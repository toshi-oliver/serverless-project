import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('demo-sls-person')


def get(event, context):
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'])
    }

    return response
