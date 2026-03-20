import pandas as pd

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Standardizes dataframe column names to lowercase and underscores."""
    df.columns = [c.lower().replace(' ', '_').strip() for c in df.columns]
    return df

def currency_formatter(value: float) -> str:
    """Formats a float as a human-readable currency string."""
    return f"${value:,.2f}"