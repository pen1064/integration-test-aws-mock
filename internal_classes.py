from typing import Optional
from pydantic import BaseModel


class DynamodbPutRequest(BaseModel):
    key: str
    value: Optional [int]


class SumRequest(BaseModel):
    a: int
    b: int

class DynamodbGetRequest(BaseModel):
    key: str
