from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import BigInteger, Column, ForeignKey, Integer, Numeric, String

from app.db.connection import Base

_BENEFICIARY_ID_FK = "beneficiary.beneficiary_id"
_RENTER_ID_FK = "renter.renter_id"
_POLICY_ID_FK = "policy.policy_id"
_PRODUCT_DETAILS_ID_FK = "product_details.product_details_id"


class Beneficiary(Base):
    __tablename__ = "beneficiary"

    beneficiary_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    document = Column(BigInteger(), nullable=False)


class Renter(Base):
    __tablename__ = "renter"

    renter_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    document = Column(BigInteger(), nullable=False)


class Address(Base):
    __tablename__ = "address"

    street = Column(String, primary_key=True, index=True)
    number = Column(Integer, primary_key=True, index=True)


class ProductDetails(Base):
    __tablename__ = "product_details"

    product_details_id = Column(Integer, primary_key=True, index=True)
    product_code = Column(Integer)
    street = Column(String)
    number = Column(Integer)
    plate = Column(String)
    chassi = Column(Integer)
    model = Column(String)


class Policy(Base):
    __tablename__ = "policy"

    policy_id = Column(Integer, primary_key=True, index=True)
    beneficiary_id = Column(Integer, ForeignKey(_BENEFICIARY_ID_FK), nullable=False)
    renter_id = Column(Integer, ForeignKey(_RENTER_ID_FK), nullable=True)
    product_details_id = Column(
        Integer, ForeignKey(_PRODUCT_DETAILS_ID_FK), nullable=False
    )


class Bill(Base):
    __tablename__ = "bill"

    bill_id = Column(Integer, primary_key=True, index=True)
    policy_id = Column(Integer, ForeignKey(_POLICY_ID_FK), index=True)
    installments = Column(Integer)
    total_value = Column(Numeric(10, 2))
    per_month = Column(Numeric(10, 2))
