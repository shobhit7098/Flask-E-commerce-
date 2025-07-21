from database import products_collection, orders_collection
from models import serialize_doc
from bson import ObjectId
import re


async def create_product(product: dict):
    result = await products_collection.insert_one(product)
    product["_id"] = result.inserted_id
    return serialize_doc(product)


async def list_products(name: str = None, size: str = None, limit: int = 10, offset: int = 0):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["size"] = size

    cursor = products_collection.find(query).skip(offset).limit(limit)
    docs = await cursor.to_list(length=limit)
    return [serialize_doc(d) for d in docs]


async def create_order(order: dict):
    result = await orders_collection.insert_one(order)
    order["_id"] = result.inserted_id
    return serialize_doc(order)


async def list_orders(user_id: str, limit: int = 10, offset: int = 0):
    query = {"user_id": user_id}
    cursor = orders_collection.find(query).skip(offset).limit(limit)
    docs = await cursor.to_list(length=limit)
    return [serialize_doc(d) for d in docs]
