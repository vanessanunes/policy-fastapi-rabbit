from typing import Annotated
from bson import ObjectId
from pydantic import BeforeValidator, PlainSerializer


def validate_object_id(v: any) -> ObjectId:
    if isinstance(v, ObjectId):
        return v
    if isinstance(v, str) and ObjectId.is_valid(v):
        return ObjectId(v)
    raise ValueError("Invalid ObjectId")


PyObjectId = Annotated[
    ObjectId,
    BeforeValidator(validate_object_id),
    PlainSerializer(lambda v: str(v), return_type=str),
]
