# data_filter.py

import pandas as pd
from datetime import datetime

def filter_data_by_analysis_type(df: pd.DataFrame, start_date: str, analysis_type: str):
    # Convert start_date to datetime object
    start_date = datetime.strptime(start_date, "%Y-%m-%d")

    # Extract year, month, and quarter from start_date
    year = start_date.year
    month = start_date.month
    quarter = (start_date.month - 1) // 3 + 1

    # Filter data based on analysis_type
    if analysis_type == "monthly":
        # Filter data for the specified month
        df_filtered = df[(pd.to_datetime(df['Date']).dt.year == year) & (pd.to_datetime(df['Date']).dt.month == month)]
    elif analysis_type == "quarterly":
        # Filter data for the specified quarter
        df_filtered = df[(pd.to_datetime(df['Date']).dt.year == year) & (pd.to_datetime(df['Date']).dt.quarter == quarter)]
    elif analysis_type == "yearly":
        # Filter data for the specified year
        df_filtered = df[pd.to_datetime(df['Date']).dt.year == year]
    else:
        # Handle unsupported analysis type
        raise ValueError("Unsupported analysis type. Supported types are 'monthly', 'quarterly', or 'yearly'.")

    # Check if data is missing
    if df_filtered.empty:
        raise ValueError("Data not available for the chosen period. Please choose another period.")

    return df_filtered
