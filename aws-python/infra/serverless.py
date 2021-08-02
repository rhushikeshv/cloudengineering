# Copyright 2016-2021, Pulumi Corporation. All rights reserved

from typing import List
import pulumi
import json
import pulumi_aws as aws
from pulumi_aws.apigatewayv2 import ApiCorsConfigurationArgs


def createAPI(funcname, lambdafunc, protocol, routekey):
    # Set up the API Gateway
    corsconfig = ApiCorsConfigurationArgs(
        allow_origins=["*"], allow_headers=["Access-Control-Allow-Origin"])
    return aws.apigatewayv2.Api(funcname, protocol_type=protocol, route_key=routekey,
                                target=lambdafunc.invoke_arn, cors_configuration=corsconfig)


def createLambdaFunction(lambdaFunction, lambda_role, runtime, codePath, handlerfunction):
    # Create the lambda to execute & attach the role to the lambda
    return aws.lambda_.Function(lambdaFunction,
                                code=pulumi.AssetArchive({
                                    ".": pulumi.FileArchive(codePath)}),
                                runtime=runtime,
                                role=lambda_role.arn,
                                handler=handlerfunction)


def createPermission4APIGateway(lambdaPermission, action, principal, lambdaFunction):
    # Give API Gateway permissions to invoke the Lambda
    return aws.lambda_.Permission(lambdaPermission,
                                  action=action,
                                  principal=principal,
                                  function=lambdaFunction)


def createLambdaAndAPIGateway(lambdaFunctionName, lambda_role, platform,
                              appFolderPath, appFuncName, lambdaPermission):

    lambdaFunction = createLambdaFunction(lambdaFunctionName,
                                          lambda_role,
                                          platform,
                                          appFolderPath,
                                          appFuncName)

    # Give API Gateway permissions to invoke the Lambda
    lambda_permission = createPermission4APIGateway(lambdaPermission,
                                                    "lambda:InvokeFunction",
                                                    "apigateway.amazonaws.com",
                                                    lambdaFunction)

    return lambdaFunction


def createDynamoDBPolicy():
    return aws.iam.Policy("dynamodbPolicy4Serverless", policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Action": ["dynamodb:*", "dax:*"],
            "Effect": "Allow",
            "Resource": "*",
        }],
    }))


def createLambdaPolicy():
    return aws.iam.Policy("lambdaPolicy4Serveless", policy=json.dumps({
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


def create_serverless_api():
    # Create the role for the Lambda to assume

    dynamodb_full_access_policy = createDynamoDBPolicy()
    lambda_basic_exec_policy = createLambdaPolicy()

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

    # drawingLambdaFunction = createLambdaFunction("drawingLambdaFunction",
    #                                             lambda_role,
    #                                             "nodejs12.x",
    #                                             "./app",
    #                                             "part.handler")

    # Give API Gateway permissions to invoke the Lambda
    # lambda_permission = createPermission4APIGateway("drawingLambdaPermission",
    #                                               "lambda:InvokeFunction",
    #                                              "apigateway.amazonaws.com",
    #                                             drawingLambdaFunction)

    drawingLambdaFunction = createLambdaAndAPIGateway("drawingLambdaFunction",
                                                      lambda_role, "nodejs12.x",
                                                      "./app", "part.handler",
                                                      "drawingLambdaPermission")

    apigw_getallparts = createAPI(
        "GetAllParts", drawingLambdaFunction, "HTTP", "GET /parts")
    apigw_get_part_by_id = createAPI(
        "GetPartById", drawingLambdaFunction, "HTTP", "GET /parts/{partnumber}")
    apigw_updated_parts = createAPI(
        "UpdateParts", drawingLambdaFunction, "HTTP", "PUT /parts")
    apigw_delete_parts = createAPI(
        "DeleteParts", drawingLambdaFunction, "HTTP", "DELETE /parts/{partnumber}")

    # Export the API endpoint for easy access
    pulumi.export("GetAllparts", apigw_getallparts.api_endpoint)
    pulumi.export("GetPartById", apigw_get_part_by_id.api_endpoint)
    pulumi.export("UpdateParts", apigw_updated_parts.api_endpoint)
    pulumi.export("DeletePartById", apigw_delete_parts.api_endpoint)
