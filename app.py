from fastapi import FastAPI

from internal_classes import SumRequest, DynamodbPutRequest, DynamodbGetRequest
from helper_functions import create_dynamodb
app = FastAPI()

dynamodb_cache = create_dynamodb()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/sum")
async def put_dynamodb(request: SumRequest):
    return {"message": request.a + request.b}

@app.put("/put_dynamodb")
async def put_dynamodb(request: DynamodbPutRequest):
    key = request.key
    value = request.value
    try:
        dynamodb_cache.put_item(Item={'key': key,'value': value})
        return {"message": f"Success to put {key} to dynamodb"}
    except:
        return {"message": f"Fail to put {key} to dynamodb"}


@app.put("/get_dynamodb")
async def get_dynamodb(request: DynamodbGetRequest):
    key = request.key
    try:
        response = dynamodb_cache.get_item(Key={'key': key})
        value = response.get("Item").get("value")
        return {"message": f"Success to get key {key} from dynamodb with value {value}"}
    except:
        return {"message": f"Fail to get {key} to dynamodb"}
