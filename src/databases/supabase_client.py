from supabase import create_client, Client
from configs.settings import Config
from src.utils.exceptions import DatabaseConnectionError
import pandas as pd

class SupabaseService:
    def __init__(self):
        try:
            self.client: Client = create_client(Config.SUPABASE_URL, Config.SUPABASE_KEY)
            print("🔗 Connected to Supabase (PostgreSQL)")
        except Exception as e:
            raise DatabaseConnectionError("Supabase", str(e))

    def fetch_all_orders(self, table_name="orders"):
        """Fetches all records from the orders table and returns a DataFrame."""
        try:
            # Querying SQL via Supabase API
            response = self.client.table(table_name).select("*").execute()
            
            # Convert JSON response to Pandas DataFrame
            df = pd.DataFrame(response.data)
            return df
        except Exception as e:
            print(f"❌ Error fetching SQL data: {e}")
            return pd.DataFrame() # Return empty DF on failure