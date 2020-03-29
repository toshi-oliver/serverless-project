import boto3

dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table('demo-sls-person')

def get_person(id):
    response = table.get_item(
            Key={
                'person_id': id
            }
        )
    return response['Item']

def hello(event, context):
    person = get_person('001')
    return person