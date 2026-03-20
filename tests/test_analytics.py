import pytest
import pandas as pd
import numpy as np
from src.analytics.engine import AnalyticsEngine
from src.analytics.processor import DataProcessor

# --- FIXTURES: Reusable data for tests ---
@pytest.fixture
def sample_data():
    """Provides a controlled DataFrame for testing math logic."""
    data = {
        'product_id': ['P1', 'P2', 'P1'],
        'amount': [100.0, 200.0, 300.0],
        'category': ['Electronics', 'Furniture', 'Electronics']
    }
    return pd.DataFrame(data)

# --- TEST CASES ---

def test_calculate_summary_stats(sample_data):
    """Verifies that the AnalyticsEngine calculates mean and sum correctly."""
    engine = AnalyticsEngine()
    stats = engine.calculate_summary_stats(sample_data)
    
    # Asserting known outcomes
    assert stats["Total Revenue"] == 600.0
    assert stats["Average Transaction"] == 200.0
    assert stats["Transaction Count"] == 3
    assert isinstance(stats["Revenue Volatility"], float)

def test_empty_dataframe_handling():
    """Ensures the engine doesn't crash on empty data."""
    empty_df = pd.DataFrame()
    engine = AnalyticsEngine()
    stats = engine.calculate_summary_stats(empty_df)
    
    assert stats == {}

def test_merge_retail_data_logic():
    """Verifies the DataProcessor correctly joins two DataFrames."""
    orders = pd.DataFrame({'product_id': ['P1'], 'amount': [100]})
    products = pd.DataFrame({'product_id': ['P1'], 'name': ['Test Product']})
    
    processor = DataProcessor()
    merged = processor.merge_retail_data(orders, products)
    
    assert not merged.empty
    assert 'name' in merged.columns
    assert merged.iloc[0]['name'] == 'Test Product'