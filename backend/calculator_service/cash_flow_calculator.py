# cash_flow_calculator.py

import pandas as pd
from backend.data_service.data_filter import filter_data_by_analysis_type

def calculate_cash_flow(pnl_df: pd.DataFrame, wc_df: pd.DataFrame, start_date: str, analysis_type: str):
    # Filter P&L data based on start date and analysis type
    pnl_filtered = filter_data_by_analysis_type(pnl_df, start_date, analysis_type)

    # Filter working capital data based on start date and analysis type
    wc_filtered = filter_data_by_analysis_type(wc_df, start_date, analysis_type)

    # Calculate net income
    net_income = pnl_filtered['Net_Income'].sum()

    # Calculate depreciation
    depreciation = pnl_filtered['Depreciation'].sum()

    # Calculate changes in working capital components
    inventory_change = wc_filtered['Inventory'].diff().sum()
    accounts_receivable_change = wc_filtered['Accounts_Receivable'].diff().sum()
    accounts_payable_change = wc_filtered['Accounts_Payable'].diff().sum()

    # Calculate cash flow from operations
    cash_flow_operations = net_income + depreciation - (inventory_change + accounts_receivable_change - accounts_payable_change)

    return cash_flow_operations

# cash_flow_calculator.py -> calculate_additional_ratios


# cash_flow_calculator.py

import pandas as pd
from backend.data_service.data_filter import filter_data_by_analysis_type

def calculate_additional_ratios(pnl_df: pd.DataFrame, wc_df: pd.DataFrame, start_date: str, analysis_type: str):
    # Filter P&L data based on start date and analysis type
    pnl_filtered = filter_data_by_analysis_type(pnl_df, start_date, analysis_type)

    # Filter working capital data based on start date and analysis type
    wc_filtered = filter_data_by_analysis_type(wc_df, start_date, analysis_type)

    # Calculate current ratio
    current_assets = wc_filtered['Inventory'] + wc_filtered['Accounts_Receivable']
    current_liabilities = wc_filtered['Accounts_Payable']
    current_ratio = current_assets.mean() / current_liabilities.mean()
    
    # Calculate quick ratio
    quick_assets = wc_filtered['Accounts_Receivable']
    quick_ratio = quick_assets.mean() / current_liabilities.mean()
    
    # Calculate inventory turnover ratio
    cost_of_goods_sold = pnl_filtered['Cost_of_Sales'].sum()
    average_inventory = wc_filtered['Inventory'].mean()
    inventory_turnover_ratio = cost_of_goods_sold / average_inventory
    
    # Construct a dictionary to hold the computed ratios
    additional_ratios = {
        "analysis_type": analysis_type,
        "start_date": start_date,
        "current_ratio": current_ratio,
        "quick_ratio": quick_ratio,
        "inventory_turnover_ratio": inventory_turnover_ratio
    }
    
    return additional_ratios
