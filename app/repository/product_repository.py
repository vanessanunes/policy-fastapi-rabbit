from fastapi import Depends
from app.db.connection import DBConnection

from app.models import data_definition

from app.models.domain import (
    Address,
    Beneficiary,
    Information,
    Values,
    Renter,
)


class ProductRepository:
    def __init__(self, database=Depends(DBConnection)) -> None:
        self.session = database.get_session()

    async def create_property_details(
        self, product_code: int, product_details: Address
    ) -> int:
        data_insert = data_definition.ProductDetails(
            product_code=product_code,
            street=product_details.street,
            number=product_details.number,
        )
        self.session.add(data_insert)
        self.session.commit()
        return data_insert.product_details_id

    async def create_vehicle_details(
        self, product_code: int, product_details: Information
    ) -> int:
        data_insert = data_definition.ProductDetails(
            product_code=product_code,
            plate=product_details.plate,
            chassi=product_details.chassis,
            model=product_details.model,
        )
        self.session.add(data_insert)
        self.session.commit()
        return data_insert.product_details_id

    async def create_beneficiary(self, beneficiary: Beneficiary) -> int:
        data_insert = data_definition.Beneficiary(
            name=beneficiary.name, document=beneficiary.cnpj
        )
        self.session.add(data_insert)
        self.session.commit()
        return data_insert.beneficiary_id

    async def create_renter(self, renter: Renter) -> int:
        data_insert = data_definition.Renter(name=renter.name, document=renter.cpf)
        self.session.add(data_insert)
        self.session.commit()
        return data_insert.renter_id

    async def create_policy(
        self,
        beneficiary_id: int,
        renter_id: int,
        product_details_id: int,
    ) -> int:
        data_insert = data_definition.Policy(
            beneficiary_id=beneficiary_id,
            renter_id=renter_id,
            product_details_id=product_details_id,
        )
        self.session.add(data_insert)
        self.session.commit()
        return data_insert.policy_id

    async def create_bill(self, values: Values, policy_id: int) -> int:
        data_insert = data_definition.Bill(
            policy_id=policy_id,
            installments=values.installments,
            total_value=values.total_value,
        )
        self.session.add(data_insert)
        self.session.commit()
        return data_insert.bill_id
