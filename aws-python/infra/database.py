import pulumi
from pulumi.resource import export
import pulumi_aws as aws


def create_database():
    basic_dynamodb_table = aws.dynamodb.Table("CLOUD_PLM_PART",
                                              attributes=[
                                                  aws.dynamodb.TableAttributeArgs(
                                                      name="Partnumber",
                                                      type="S",
                                                  )

                                              ],
                                              hash_key="Partnumber",
                                              read_capacity=20,
                                              tags={
                                                  "Environment": "dev",
                                                  "Name": "part-dynamodb-table",
                                              },
                                              ttl=aws.dynamodb.TableTtlArgs(
                                                  attribute_name="TimeToLiveSpecification",
                                                  enabled=True,
                                              ),
                                              write_capacity=20)
    export('arn dynamodb table', basic_dynamodb_table.arn)
