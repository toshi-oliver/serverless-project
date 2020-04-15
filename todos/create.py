import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('demo-sls-person')


def create(event, context):
    data = json.loads(event["body"])if type(
        event["body"]) == str else event["body"]

    item = {
        "id": data["id"],
        "age": data["age"],
        "name": data["name"]
    }

    table.put_item(Item=item)

    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
