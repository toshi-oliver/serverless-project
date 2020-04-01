import os
import boto3
import json

dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table('demo-sls-person')
  
def get_person(id):
    response = table.get_item(
            Key={
                 'id': id
            }
        )
    return response['Item']

def get_persons():
    response = table.scan()
    return response['Items']

def get(event, context):
    return get_persons() if event['id'] == '' else get_person(event['id'])