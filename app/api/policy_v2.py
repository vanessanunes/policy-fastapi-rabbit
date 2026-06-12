from fastapi import APIRouter, Depends
from pymongo.asynchronous.database import (
    AsyncDatabase,
)
from app.core.database import get_db
from app.core.schema import ResponseOK
from app.repositories.product_v2_repository import ProductV2Repository
from app.schemas.policy_schema import PolicyCreateSchema, PolicyResponseSchema
from app.services.product_v2_service import ProductV2Service

router = APIRouter(prefix="/policy", tags=["policy"])


# 1. Ajustado para async para resolver o generator do MongoDB
async def get_product_repository(
    db: AsyncDatabase = Depends(get_db),
) -> ProductV2Repository:
    return ProductV2Repository(db)


# 2. Ajustado para receber a instância correta do repositório
def get_product_service(
    repo: ProductV2Repository = Depends(get_product_repository),
) -> ProductV2Service:
    return ProductV2Service(repo)


@router.post("/", response_model=ResponseOK[PolicyResponseSchema], status_code=201)
async def create(
    product: PolicyCreateSchema,
    service: ProductV2Service = Depends(get_product_service),
):
    data = await service.create(product)
    return ResponseOK(data=data)
