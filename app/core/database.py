from pymongo import AsyncMongoClient

from app.core.settings import get_settings

settings = get_settings

MONGO_URI = settings.mongodb_url
DATABASE_NAME = settings.database_name


class MongoConnection:
    def __init__(self) -> None:
        self.client: AsyncMongoClient = None
        self.db = None

    def connect(self):
        self.client = AsyncMongoClient(MONGO_URI)
        self.db = self.client[DATABASE_NAME]

    def disconnect(self):
        """Fecha a conexão (útil para o shutdown da API)"""
        if self.client:
            self.client.close()
            print("🛑 Conexão com o MongoDB encerrada.")


mongo_manager = MongoConnection()


async def get_db():
    return mongo_manager.db
