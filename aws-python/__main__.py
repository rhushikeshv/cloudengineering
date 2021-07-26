from infra.s3_frontend import *
from infra.lambda_backend import *
from infra.serverless import *
from infra.database import *

create_s3_frontend()
create_serverless_api()
create_database()


