const AWS = require("aws-sdk");

const dynamo = new AWS.DynamoDB.DocumentClient();

const tableName ="CLOUD_PLM_ECR-fd9ee69";

exports.handler = async (event, context) => {
  let body;
  let statusCode = 200;
  const headers = {
    "Content-Type": "application/json"
  };
  try {
    switch (event.routeKey) {
      case "DELETE /ecrs/{change}":
        await dynamo
          .delete({
            TableName: tableName,
            Key: {
              'Enggchange': event.pathParameters.change
            }
          })
          .promise();
        body = `Deleted ECR ${change}`;
        break;
      case "GET /ecrs/{change}":
        console.log("--Get ecrs/for engg change called --" + event.pathParameters);
        body = await dynamo
          .get({
            TableName: tableName,
            Key: {
              'Enggchange': event.pathParameters.change
            }
          })
          .promise();
        break;
      case "GET /ecrs":
        body = await dynamo.scan({ TableName: tableName }).promise();
        break;
      case "PUT /ecrs":
        let requestJSON = JSON.parse(event.body);
        await dynamo
          .put({
            TableName: tableName,
            parts: {
              "Enggchange": requestJSON.change.toString()
            }
          })
          .promise();
        body = `Put ECR ${requestJSON.change.toString()}`;
        break;
      default:
        throw new Error(`Unsupported route: "${event.routeKey}"`);
    }
  } catch (err) {
    statusCode = 400;
    body = err.message;
  } finally {
    body = JSON.stringify(body);
  }
  return {
    statusCode,
    body,
    headers
  };
};
