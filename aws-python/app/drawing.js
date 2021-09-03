const AWS = require("aws-sdk");

const dynamo = new AWS.DynamoDB.DocumentClient();

const tableName ="CLOUD_PLM_DRAWING-00e391a";

exports.handler = async (event, context) => {
  let body;
  let statusCode = 200;
  const headers = {
    "Content-Type": "application/json"
  };
  try {
    switch (event.routeKey) {
      case "DELETE /drawings/{drawingtitle}":
        await dynamo
          .delete({
            TableName: tableName,
            Key: {
              'Drawingtitle': event.pathParameters.drawingtitle
            }
          })
          .promise();
        body = `Deleted drawing ${drawingtitle}`;
        break;
      case "GET /drawings/{drawingtitle}":
        console.log("--Get Drawings/for drawing title called --" + event.pathParameters);
        body = await dynamo
          .get({
            TableName: tableName,
            Key: {
              'Drawingtitle': event.pathParameters.drawingtitle
            }
          })
          .promise();
        break;
      case "GET /drawings":
        body = await dynamo.scan({ TableName: tableName }).promise();
        break;
      case "PUT /drawings":
        let requestJSON = JSON.parse(event.body);
        await dynamo
          .put({
            TableName: tableName,
            parts: {
              "Drawingtitle": requestJSON.drawingtitle.toString()
            }
          })
          .promise();
        body = `Put Drawing ${requestJSON.drawingtitle.toString()}`;
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
