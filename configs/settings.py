import os
from dotenv import load_dotenv

# Load the .env file automatically
load_dotenv()

class Config:
    """Centralized configuration for the Omni-Store Project"""
    # Supabase Config
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    
    # MongoDB Config
    MONGO_URI = os.getenv("MONGO_URI")
    MONGO_DB_NAME = "omni_store" 
    
    # File Paths (relative to root)
    RAW_DATA_PATH = "data/raw/"
    PROCESSED_DATA_PATH = "data/processed/"
    LOG_FILE = "logs/app.log"

    @staticmethod
    def validate_config():
        """A quick helper to ensure we aren't missing any keys"""
        required = ["SUPABASE_URL", "SUPABASE_KEY", "MONGO_URI"]
        for key in required:
            if not getattr(Config, key):
                print(f"❌ Missing environment variable: {key}")
                return False
        print("✅ Environment variables loaded successfully.")
        return True