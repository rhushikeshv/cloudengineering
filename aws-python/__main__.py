from infra.s3_frontend import *
from infra.lambda_backend import *
from infra.serverless import *
from infra.database import *

create_s3_frontend() # hosting a static web site or angular app , that is streamed to browser
# this has the lambda func to greet (lambda exposed over REST API Gateway)
# this api will need security tokens like OAuth2/JWT
create_serverless_api() # this will need iam role and policy to access dynamodb
create_database()


