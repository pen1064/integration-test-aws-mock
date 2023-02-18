from moto import mock_dynamodb
import boto3

def create_dynamodb():
    mock = mock_dynamodb()
    mock.start()

    dynamodb_resource =boto3.resource('dynamodb')

    table_name = 'test-playground'
    table = dynamodb_resource.create_table(
        TableName=table_name,
        KeySchema=[{'AttributeName': 'key', 'KeyType':'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'key', 'AttributeType': 'S'}],
        BillingMode='PAY_PER_REQUEST'
    )
    return table

def destroy_dynamodb():
    mock = mock_dynamodb()
    mock.stop()
