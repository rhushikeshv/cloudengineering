const AWS = require("aws-sdk");

const dynamo = new AWS.DynamoDB.DocumentClient();

const tableName ="CLOUD_PLM_PART-efc77c7";

exports.handler = async (event, context) => {
  let body;
  let statusCode = 200;
  const headers = {
    "Content-Type": "application/json"
  };
  try {
    switch (event.routeKey) {
      case "DELETE /parts/{partnumber}":
        await dynamo
          .delete({
            TableName: tableName,
            Key: {
              'Partnumber': event.pathParameters.partnumber
            }
          })
          .promise();
        body = `Deleted part ${partnumber}`;
        break;
      case "GET /parts/{partnumber}":
        console.log("--Get Parts/for id called --" + event.pathParameters);
        body = await dynamo
          .get({
            TableName: tableName,
            Key: {
              'Partnumber': event.pathParameters.partnumber
            }
          })
          .promise();
        break;
      case "GET /parts":
        body = await dynamo.scan({ TableName: tableName }).promise();
        break;
      case "PUT /parts":
        let requestJSON = JSON.parse(event.body);
        await dynamo
          .put({
            TableName: tableName,
            parts: {
              "Partnumber": requestJSON.partnumber.toString()
            }
          })
          .promise();
        body = `Put Part ${requestJSON.partnumber.toString()}`;
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
