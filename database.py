from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING

MONGO_URI = "mongodb+srv://avirajbharadwaj6395:Av9GPANelR3IEa7t@cluster1.rt6sscq.mongodb.net/"  # Replace with actual MongoDB Atlas URI
client = AsyncIOMotorClient(MONGO_URI)
db = client["ecommerce"]

products_collection = db["products"]
orders_collection = db["orders"]

# Create indexes
async def init_indexes():
    await products_collection.create_index([("name", ASCENDING)])
    await orders_collection.create_index([("user_id", ASCENDING)])
