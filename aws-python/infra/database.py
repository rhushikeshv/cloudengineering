import pulumi
from pulumi.resource import export
import pulumi_aws as aws


def create_part_table():
    basic_part_table = aws.dynamodb.Table("CLOUD_PLM_PART",
                                          attributes=[
                                              aws.dynamodb.TableAttributeArgs(
                                                  name="Partnumber",
                                                  type="S",
                                              )

                                          ],
                                          hash_key="Partnumber",
                                          billing_mode="PAY_PER_REQUEST",

                                          tags={
                                              "Environment": "dev",
                                              "Name": "part-dynamodb-table",
                                          },
                                          ttl=aws.dynamodb.TableTtlArgs(
                                              attribute_name="TimeToLiveSpecification",
                                              enabled=True,
                                          ),
                                          )
    export('arn part table ', basic_part_table.arn)


def create_dwg_table():
    basic_dwg_table = aws.dynamodb.Table("CLOUD_PLM_DRAWING",
                                         attributes=[
                                             aws.dynamodb.TableAttributeArgs(
                                                 name="Drawingtitle",
                                                 type="S",
                                             )

                                         ],
                                         hash_key="Drawingtitle",
                                         billing_mode="PAY_PER_REQUEST",

                                         tags={
                                                  "Environment": "dev",
                                                  "Name": "dwg-dynamodb-table",
                                         },
                                         ttl=aws.dynamodb.TableTtlArgs(
                                             attribute_name="TimeToLiveSpecification",
                                             enabled=True,
                                         ),
                                         )
    export('arn drawing table', basic_dwg_table.arn)
    
def create_ecr_table():
    basic_ecr_table = aws.dynamodb.Table("CLOUD_PLM_ECR",
                                         attributes=[
                                             aws.dynamodb.TableAttributeArgs(
                                                 name="Enggchange",
                                                 type="S",
                                             )

                                         ],
                                         hash_key="Enggchange",
                                         billing_mode="PAY_PER_REQUEST",

                                         tags={
                                                  "Environment": "dev",
                                                  "Name": "dwg-dynamodb-table",
                                         },
                                         ttl=aws.dynamodb.TableTtlArgs(
                                             attribute_name="TimeToLiveSpecification",
                                             enabled=True,
                                         ),
                                         )
    export('arn ecr table', basic_ecr_table.arn)
