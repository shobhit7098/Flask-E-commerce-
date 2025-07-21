from fastapi import APIRouter, Query, Path
from typing import List
from models import OrderCreate, OrderResponse
import crud

router = APIRouter()

@router.post("/orders", response_model=OrderResponse, status_code=201)
async def create_order(order: OrderCreate):
    created = await crud.create_order(order.dict())
    return created


@router.get("/orders/{user_id}", response_model=List[OrderResponse])
async def get_orders(
    user_id: str = Path(...),
    limit: int = Query(10, gt=0),
    offset: int = Query(0, ge=0),
):
    orders = await crud.list_orders(user_id=user_id, limit=limit, offset=offset)
    return orders
