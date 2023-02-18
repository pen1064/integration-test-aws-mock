# Integration Test Exploration
First create an app to have some interaction with DynamoDB.

Try out following:
1. using moto to mock DynamoDB to perform unittest -> `unit_test_dynamodb.py`
2. using Fastapi.TestClient and moto to perform integration test -> `integration_test.py`
