from typing import Annotated

from app.repositories.product_v2_repository import ProductV2Repository
from app.schemas.policy_schema import PolicyCreateSchema


class ProductV2Service:
    def __init__(
        self,
        repo: ProductV2Repository,
    ) -> None:
        self.repo = repo

    async def create(self, product: PolicyCreateSchema) -> Annotated[dict, None]:
        product_dict = product.model_dump()
        inserted_id = await self.repo.save(product_dict)
        product_dict["id"] = inserted_id
        return product_dict
