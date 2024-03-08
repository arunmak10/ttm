import pytest
from unittest.mock import MagicMock, patch
from backend.calculator_service.cash_flow_calculator import calculate_cash_flow, calculate_additional_ratios
import pandas as pd
from tests.backend.dummy_data_provider import get_dummy_data


@pytest.fixture
def mock_filter_data_by_analysis_type():
    with patch('backend.calculator_service.cash_flow_calculator.filter_data_by_analysis_type') as mock_filter:
        yield mock_filter

def test_calculate_cash_flow(mock_filter_data_by_analysis_type: MagicMock):
    # Mock dataframes
    pnl_df = get_dummy_data()
    wc_df = get_dummy_data('wcf')

    # Set up mock filter_data_by_analysis_type behavior
    mock_filter_data_by_analysis_type.side_effect = lambda df, start_date, analysis_type: df

    # Call the method under test
    monthly_cash_flow_operations = calculate_cash_flow(pnl_df, wc_df, "2022-01-01", "monthly")
    quarterly_cash_flow_operations = calculate_cash_flow(pnl_df, wc_df, "2022-01-01", "quarterly")
    yearly_cash_flow_operations = calculate_cash_flow(pnl_df, wc_df, "2022-01-01", "yearly")

    # Assert the results
    assert (quarterly_cash_flow_operations, monthly_cash_flow_operations, yearly_cash_flow_operations) == (156583.1964974503,156583.1964974503,156583.1964974503)
    

def test_calculate_additional_ratios(mock_filter_data_by_analysis_type: MagicMock):
    # Mock dataframes
    pnl_df = get_dummy_data()
    wc_df = get_dummy_data('wcf')

    # Set up mock filter_data_by_analysis_type behavior
    mock_filter_data_by_analysis_type.side_effect = lambda df, start_date, analysis_type: df

    # Call the method under test
    additional_ratios = calculate_additional_ratios(pnl_df, wc_df, "2022-01-01", "monthly")

    # Assert the result or behavior as needed
    assert additional_ratios is not None

if __name__ == "__main__":
    pytest.main()
