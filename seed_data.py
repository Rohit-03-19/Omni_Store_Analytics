import random
from datetime import datetime, timedelta
from src.databases.supabase_client import SupabaseService
from src.databases.mongo_client import MongoService

def seed_databases():
    print("🌱 Starting Data Seed Process...")

    # 1. Initialize Services
    sql = SupabaseService()
    nosql = MongoService()

    # --- PART A: SEED MONGODB (Product Metadata) ---
    # In industry, NoSQL handles the flexible "Catalog"
    products = [
        {"product_id": "P001", "name": "Quantum Laptop", "category": "Electronics", "tags": ["high-end", "workstation"]},
        {"product_id": "P002", "name": "Ergo Chair", "category": "Furniture", "tags": ["office", "ergonomic"]},
        {"product_id": "P003", "name": "Mechanical Keyboard", "category": "Electronics", "tags": ["rgb", "gaming"]},
        {"product_id": "P004", "name": "Smart Water Bottle", "category": "Lifestyle", "tags": ["iot", "health"]},
        {"product_id": "P005", "name": "Standing Desk", "category": "Furniture", "tags": ["adjustable", "wood"]}
    ]

    print("🍃 Injecting Products into MongoDB...")
    nosql.db["products"].delete_many({}) # Clear old data
    nosql.db["products"].insert_many(products)

    # --- PART B: SEED SUPABASE (Transactional Orders) ---
    # SQL handles the rigid "Money" transactions
    orders = []
    product_ids = ["P001", "P002", "P003", "P004", "P005"]
    
    print("🔗 Generating Orders for Supabase...")
    for i in range(20):
        order = {
            "product_id": random.choice(product_ids),
            "amount": round(random.uniform(50, 2000), 2),
            "customer_id": f"CUST_{random.randint(100, 999)}",
            "created_at": (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat()
        }
        orders.append(order)

    # Note: Ensure your 'orders' table in Supabase has these columns!
    try:
        sql.client.table("orders").insert(orders).execute()
        print("✅ SQL Orders Injected Successfully.")
    except Exception as e:
        print(f"❌ SQL Injection Failed: {e}")

    print("\n✨ Database Seeding Complete! You can now run 'python main.py'.")

if __name__ == "__main__":
    seed_databases()