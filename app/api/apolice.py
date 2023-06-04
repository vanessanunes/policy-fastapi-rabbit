from fastapi import APIRouter, Depends, HTTPException

from app.models.domain import Product

from app.service.product_service import ProductService

router = APIRouter(prefix="/policy", tags=["policy"])


PRODUCTS = {
    111: "property",
    222: "vehicle",
}


@router.post("/")
async def policy_generator(product: Product, service: ProductService = Depends()):
    product_type = product.item.name().lower()
    product_id = product.product
    if not product_type == PRODUCTS.get(product_id):
        raise HTTPException(
            status_code=404,
            detail=f"Product not compatible {product_type=}, {product_id=}",
        )
    await service.save(product, product_id)
    return HTTPException(
        status_code=200,
        detail="aaa",
    )
