import numpy as np
import pandas as pd

class AnalyticsEngine:
    """
    Handles the heavy mathematical lifting using NumPy.
    """
    @staticmethod
    def calculate_summary_stats(df: pd.DataFrame):
        if df.empty:
            return {}

        # Using NumPy for performance on numeric columns
        amounts = df['amount'].values
        
        # Demonstrating statistical functions
        stats = {
            "Total Revenue": np.sum(amounts),
            "Average Transaction": np.mean(amounts),
            "Revenue Volatility": np.std(amounts), # Standard Deviation
            "Transaction Count": len(amounts)
        }
        
        return stats