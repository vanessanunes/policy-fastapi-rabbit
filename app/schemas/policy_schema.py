from pydantic import BaseModel, ConfigDict, Field

from app.core.types import PyObjectId
from app.enums.product_enum import ProductCodeEnum


class PolicyCreateSchema(BaseModel):
    code: ProductCodeEnum


class PolicyResponseSchema(PolicyCreateSchema):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True)
    id: PyObjectId = Field(alias="_id")
