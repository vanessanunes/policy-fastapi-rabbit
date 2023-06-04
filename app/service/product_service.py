from fastapi import Depends
from app.models.domain import Product
from app.repository.product_repository import ProductRepository


class ProductService:
    def __init__(
        self,
        repo: ProductRepository = Depends(),
    ) -> None:
        self.repo = repo

    async def save(self, product: Product, product_type_id: int):
        id_renter = None
        if product_type_id == 222:
            id_details = await self.repo.create_vehicle_details(
                product_type_id, product.item.information
            )
        else:
            id_details = await self.repo.create_property_details(
                product_type_id, product.item.address
            )
            id_renter = await self.repo.create_renter(product.item.renter)

        id_beneficiary = await self.repo.create_beneficiary(product.item.beneficiary)
        id_policy = await self.repo.create_policy(id_beneficiary, id_renter, id_details)
        id_values = await self.repo.create_bill(product.values, id_policy)
