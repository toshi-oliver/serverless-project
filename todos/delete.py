import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('demo-sls-person')


def delete(event, context):
    # delete the todo from the database
    table.delete_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # create a response
    response = {
        "statusCode": 200
    }

    return response
