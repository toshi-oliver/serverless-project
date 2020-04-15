import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('demo-sls-person')


def update(event, context):
    data = json.loads(event["body"])
    result = table.update_item(
        Key={
            'id': event['pathParameters']['id']
        },
        ExpressionAttributeNames={
            '#todo_name': 'name',
        },
        ExpressionAttributeValues={
            ':name': data['name'],
            ':age': data['age']
        },
        UpdateExpression='SET #todo_name = :name,'
                         'age=:age',
        ReturnValues="ALL_NEW",
    )
    response = {
        'statusCode': 200,
        'body': json.dumps(result['Attributes'])
    }

    return response
