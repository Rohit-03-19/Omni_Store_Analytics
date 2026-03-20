import pandas as pd
from src.utils.decorators import monitor_performance
from src.utils.exceptions import ProcessingError

class DataProcessor:
    @monitor_performance
    def merge_retail_data(self, orders_df: pd.DataFrame, products_df: pd.DataFrame):
        """
        Merges SQL-based order data with NoSQL-based product metadata.
        This is the core 'Hybrid' logic.
        """
        try:
            if orders_df.empty or products_df.empty:
                raise ProcessingError("One or more input DataFrames are empty.")

            # Ensure product_id is the same type across both
            orders_df['product_id'] = orders_df['product_id'].astype(str)
            products_df['product_id'] = products_df['product_id'].astype(str)

            # Left join: Keep all orders and add product info where available
            unified_df = pd.merge(orders_df, products_df, on='product_id', how='left')
            
            return unified_df
        except Exception as e:
            print(f"❌ Error during data merge: {e}")
            return pd.DataFrame()