import pulumi
import pulumi_aws as aws


def create_database():
    basic_dynamodb_table = aws.dynamodb.Table("part",
                                              attributes=[
                                                  aws.dynamodb.TableAttributeArgs(
                                                      name="Partnumber",
                                                      type="S",
                                                  ),
                                                  aws.dynamodb.TableAttributeArgs(
                                                      name="Partname",
                                                      type="S",
                                                  )

                                              ],
                                              billing_mode="PROVISIONED",
                                              global_secondary_indexes=[aws.dynamodb.TableGlobalSecondaryIndexArgs(
                                                  hash_key="Partname",
                                                  name="PartnameIndex",
                                                  non_key_attributes=["Partnumber"],
                                                  projection_type="INCLUDE",
                                                  read_capacity=10,
                                                  write_capacity=10,
                                              )],
                                              hash_key="Partnumber",
                                              range_key="Partname",
                                              read_capacity=20,
                                              tags={
                                                  "Environment": "dev",
                                                  "Name": "part-dynamodb-table",
                                              },
                                              ttl=aws.dynamodb.TableTtlArgs(
                                                  attribute_name="TimeToExist",
                                                  enabled=False,
                                              ),
                                              write_capacity=20)
