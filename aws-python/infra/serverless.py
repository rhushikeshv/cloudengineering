# Copyright 2016-2021, Pulumi Corporation. All rights reserved

from typing import List
import pulumi
import json
import pulumi_aws as aws
from pulumi_aws.apigatewayv2 import ApiCorsConfigurationArgs


def create_serverless_api():
    # Create the role for the Lambda to assume

    dynamodb_full_access_policy = aws.iam.Policy("dynamodbPolicy4Serverless", policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Action": ["dynamodb:*", "dax:*"],
            "Effect": "Allow",
            "Resource": "*",
        }],
    }))
    lambda_basic_exec_policy = aws.iam.Policy("lambdaPolicy4Serveless", policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Effect": "Allow",
            "Resource": "*",
        }],
    }))

    lambda_role = aws.iam.Role("lambdaRole4Serverless",
                               assume_role_policy=json.dumps({
                                   "Version": "2012-10-17",
                                   "Statement": [
                                       {
                                           "Action": "sts:AssumeRole",
                                           "Principal": {
                                               "Service": "lambda.amazonaws.com",
                                           },
                                           "Effect": "Allow",
                                           "Sid": "",
                                       },
                                   ]
                               }), managed_policy_arns=[dynamodb_full_access_policy.arn, lambda_basic_exec_policy.arn])

    # Create the lambda to execute & attach the role to the lambda
    lambda_function = aws.lambda_.Function("lambdaFunction",
                                           code=pulumi.AssetArchive({
                                               ".": pulumi.FileArchive("./app"),
                                           }),
                                           runtime="nodejs12.x",
                                           role=lambda_role.arn,
                                           handler="index.handler")

    # Give API Gateway permissions to invoke the Lambda
    lambda_permission = aws.lambda_.Permission("lambdaPermission",
                                               action="lambda:InvokeFunction",
                                               principal="apigateway.amazonaws.com",
                                               function=lambda_function)

    # Set up the API Gateway
    corsconfig = ApiCorsConfigurationArgs(allow_origins="*")

    

    
    apigw_getallparts = aws.apigatewayv2.Api("GetAllParts",
                                             protocol_type="HTTP",
                                             route_key="GET /parts",
                                             target=lambda_function.invoke_arn,
                                             cors_configuration=corsconfig.allow_headers)

    apigw_get_part_by_id = aws.apigatewayv2.Api("GetPartById",
                                                protocol_type="HTTP",
                                                route_key="GET /parts/{partnumber}",
                                                target=lambda_function.invoke_arn,
                                                cors_configuration=corsconfig.allow_headers)

    apigw_updated_parts = aws.apigatewayv2.Api("UpdateParts",
                                               protocol_type="HTTP",
                                               route_key="PUT /parts",
                                               target=lambda_function.invoke_arn,
                                               cors_configuration=corsconfig.allow_headers)

    apigw_delete_parts = aws.apigatewayv2.Api("DeleteParts",
                                              protocol_type="HTTP",
                                              route_key="DELETE /parts/{partnumber}",
                                              target=lambda_function.invoke_arn,
                                              cors_configuration=corsconfig.allow_headers)

    # Export the API endpoint for easy access
    pulumi.export("GetAllparts", apigw_getallparts.api_endpoint)
    pulumi.export("GetPartById", apigw_get_part_by_id.api_endpoint)
    pulumi.export("UpdateParts", apigw_updated_parts.api_endpoint)
    pulumi.export("DeletePartById", apigw_delete_parts.api_endpoint)
