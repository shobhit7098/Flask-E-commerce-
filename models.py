 
from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId


class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = ""
    price: float
    size: str


class ProductResponse(ProductCreate):
    id: str


class OrderItem(BaseModel):
    product_id: str
    quantity: int


class OrderCreate(BaseModel):
    user_id: str
    items: List[OrderItem]


class OrderResponse(BaseModel):
    id: str
    user_id: str
    items: List[OrderItem]


# MongoDB ObjectId conversion helper
def serialize_doc(doc):
    doc["id"] = str(doc["_id"])
    doc.pop("_id", None)
    return doc
