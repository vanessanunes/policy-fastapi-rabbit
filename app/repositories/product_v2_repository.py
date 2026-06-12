from bson import ObjectId
from pymongo.asynchronous.database import AsyncDatabase


class ProductV2Repository:
    def __init__(self, db: AsyncDatabase) -> None:
        self.collection = db["produtos"]

    async def get(self, pk: ObjectId) -> dict:
        result = self.collection.find({"_id": pk})
        return result

    async def save(self, data: dict) -> str:
        result = await self.collection.insert_one(data)
        return str(result.inserted_id)
