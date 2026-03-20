from src.databases.supabase_client import SupabaseService
from src.databases.mongo_client import MongoService
from src.analytics.processor import DataProcessor
from src.analytics.engine import AnalyticsEngine
from src.visualizations.dashboard import Visualizer

def main():
    print("🚀 Initializing Omni-Store Analytics Platform...")

    try:
        # 1. Connect to Databases
        sql_service = SupabaseService()
        nosql_service = MongoService()

        # 2. Fetch Data
        print("📥 Fetching data from Hybrid sources...")
        orders = sql_service.fetch_all_orders()
        metadata = nosql_service.fetch_product_metadata()

        # 3. Process & Merge
        processor = DataProcessor()
        unified_data = processor.merge_retail_data(orders, metadata)

        # 4. Generate Stats
        engine = AnalyticsEngine()
        stats = engine.calculate_summary_stats(unified_data)
        
        print("\n--- Key Business Metrics ---")
        for key, value in stats.items():
            print(f"{key}: {value}")

        # 5. Visualize
        Visualizer.plot_sales_by_category(unified_data)
        print("\n✅ Analytics Pipeline Completed Successfully.")

    except Exception as e:
        print(f"💥 Pipeline failed: {e}")

if __name__ == "__main__":
    main()