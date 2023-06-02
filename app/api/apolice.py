from typing import Union
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.common.rabbitmqconsumer import RabbitMqConsumer

from app.common.rabbitmqpublisher import RabbitMqPublisher
from app.config.rabbit_connection import RabbitConnection, rabbit_conn

router = APIRouter(prefix="/policy", tags=["policy"])


class Address(BaseModel):
    street: str
    number: int


class Renter(BaseModel):
    name: str
    cpf: int


class Recipient(BaseModel):
    name: str
    cnpj: int


class Property(BaseModel):
    address: Address
    renter: Renter
    recipient: Recipient

    @classmethod
    def name(cls) -> str:
        return cls.__name__


class Vehicle(BaseModel):
    plate: str
    chassis: int
    model: str
    recipient: Recipient

    @classmethod
    def name(cls) -> str:
        return cls.__name__


class Values(BaseModel):
    total_value: float
    installments: int


class Product(BaseModel):
    product: int
    item: Union[Property, Vehicle]
    values: Values


PRODUCTS = {
    111: "property",
    222: "vehicle",
}


@router.post("/")
async def policy_generator(product: Product):
    product_type = product.item.name().lower()
    product_id = product.product
    if not product_type == PRODUCTS.get(product_id):
        raise HTTPException(
            status_code=404,
            detail=f"Product not compatible {product_type=}, {product_id=}",
        )

    await rabbit_conn.send_message(product.dict(), product_type)
