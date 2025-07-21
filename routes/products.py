from fastapi import APIRouter, Query
from typing import List, Optional
from models import ProductCreate, ProductResponse
import crud

router = APIRouter()


@router.post("/products", response_model=ProductResponse, status_code=201)
async def create_product(product: ProductCreate):
    created = await crud.create_product(product.dict())
    return created


@router.get("/products", response_model=List[ProductResponse])
async def get_products(
    name: Optional[str] = None,
    size: Optional[str] = None,
    limit: int = Query(10, gt=0),
    offset: int = Query(0, ge=0),
):
    products = await crud.list_products(name=name, size=size, limit=limit, offset=offset)
    return products
