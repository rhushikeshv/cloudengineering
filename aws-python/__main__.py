from typing import Optional, Mapping

import pulumi

from pulumi_aws import s3

"""An AWS Python Pulumi program"""
"""This is a sample program to create s3 bucket"""

# add a label


# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('my-bucket', tags={
    "Environment": "Dev",
    "Name": "My bucket",
})

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)
