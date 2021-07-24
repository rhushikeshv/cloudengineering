import json
import mimetypes
import os

from pulumi import export, FileAsset
from pulumi_aws import s3


def create_s3_frontend():
    web_bucket = s3.Bucket('s3-website-bucket',
                           website=s3.BucketWebsiteArgs(
                               index_document="index.html",
                           ))

    content_dir = "www"
    for file in os.listdir(content_dir):
        filepath = os.path.join(content_dir, file)
        mime_type, _ = mimetypes.guess_type(filepath)
        obj = s3.BucketObject(file,
                              bucket=web_bucket.id,
                              source=FileAsset(filepath),
                              content_type=mime_type,
                              tags={
                                  'env': 'dev'
                              }
                              )

    def public_read_policy_for_bucket(bucket_id):
        return json.dumps({
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Principal": "*",
                "Action": [
                    "s3:GetObject"
                ],
                "Resource": [
                    f"arn:aws:s3:::{bucket_id}/*",
                ]
            }]
        })

    bucket_id = web_bucket.id
    bucket_policy = s3.BucketPolicy("bucket-policy",
                                    bucket=bucket_id,
                                    policy=bucket_id.apply(public_read_policy_for_bucket))

    # Export the name of the bucket
    export('bucket_id', web_bucket.id)
    export('website_url', web_bucket.website_endpoint)
