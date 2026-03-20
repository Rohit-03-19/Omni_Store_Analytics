from pymongo import MongoClient
from configs.settings import Config
from src.utils.exceptions import DatabaseConnectionError
import pandas as pd

class MongoService:
    def __init__(self):
        try:
            self.client = MongoClient(Config.MONGO_URI)
            self.db = self.client[Config.MONGO_DB_NAME]
            # Send a ping to confirm a successful connection
            self.client.admin.command('ping')
            print("🍃 Connected to MongoDB Atlas (NoSQL)")
        except Exception as e:
            raise DatabaseConnectionError("MongoDB", str(e))

    def fetch_product_metadata(self, collection_name="products"):
        """Fetches product details from MongoDB and returns a DataFrame."""
        try:
            collection = self.db[collection_name]
            # 'find' returns all documents. We convert the cursor to a list then a DF.
            data = list(collection.find({}, {"_id": 0})) # Exclude MongoDB's internal ID
            return pd.DataFrame(data)
        except Exception as e:
            print(f"❌ Error fetching NoSQL data: {e}")
            return pd.DataFrame()