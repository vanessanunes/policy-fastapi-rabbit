from decimal import Decimal
from typing import Union
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    number: int


class Beneficiary(BaseModel):
    name: str
    cnpj: str

    class Config:
        orm_mode = True


class Renter(BaseModel):
    name: str
    cpf: str


class Property(BaseModel):
    address: Address
    renter: Renter
    beneficiary: Beneficiary

    @classmethod
    def name(cls) -> str:
        return cls.__name__


class Information(BaseModel):
    plate: str
    chassis: int
    model: str


class Vehicle(BaseModel):
    information: Information
    beneficiary: Beneficiary

    @classmethod
    def name(cls) -> str:
        return cls.__name__


class ProductDetails(BaseModel):
    street: str = ""
    number: int = 0
    plate: str = ""
    chassi: str = ""
    model: str = ""


class Values(BaseModel):
    total_value: float
    installments: int


class Product(BaseModel):
    product: int
    item: Union[Property, Vehicle]
    values: Values
