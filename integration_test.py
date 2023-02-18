from fastapi.testclient import TestClient
from app import app


client = TestClient(app)

url_full = '/'
response = client.get(url_full)
assert response.status_code == 200
assert response.json() == {"message": "Hello World"}


url_full_sum = '/sum'
response_sum = client.post(url_full_sum, json={"a": 3, "b": 4})
assert response_sum.status_code == 200
assert response_sum.json() == {"message": 7}


url_full_put_dynamo = '/put_dynamodb'
response_put_dynamo = client.put(url_full_put_dynamo, json={"key": "test1", "value": 1234})
assert response_put_dynamo.status_code == 200
assert response_put_dynamo.json() == {"message": 'Success to put test1 to dynamodb'}


url_full_get_dynamo = '/get_dynamodb'
response_get_dynamo = client.put(url_full_get_dynamo, json={"key": "test1"})
assert response_get_dynamo.status_code == 200
assert response_get_dynamo.json() == {"message": 'Success to get key test1 from dynamodb with value 1234'}

response_get_dynamo_fail = client.put(url_full_get_dynamo, json={"key": "test3"})
assert response_get_dynamo_fail.status_code == 200
assert response_get_dynamo_fail.json() == {"message": f"Fail to get test3 to dynamodb"}
