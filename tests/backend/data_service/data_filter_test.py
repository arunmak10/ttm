import pytest
from unittest.mock import patch, MagicMock
from backend.data_service.data_filter import filter_data_by_analysis_type
from tests.backend.dummy_data_provider import get_dummy_data
import pandas as pd

def test_filter_data_by_analysis_type_monthly():
    # Mock dataframes
    dummy_pnl_df = get_dummy_data()
    #pnl_df = get_dummy_data()
    # Call the method under test
    filtered_data = filter_data_by_analysis_type(dummy_pnl_df, "2019-01-01", "monthly")

    # Assert the result
    assert len(filtered_data) > 0

    assert filtered_data['Cost_of_Sales'].sum() == 109263.1307603196

def test_filter_data_by_analysis_type_quarterly():
    # Mock dataframes
    dummy_pnl_df = get_dummy_data()
    # Call the method under test
    filtered_data = filter_data_by_analysis_type(dummy_pnl_df, "2019-01-01", "quarterly")

    # Assert the result
    assert len(filtered_data) > 0

    assert filtered_data['Cost_of_Sales'].sum() == 294751.50052640616

def test_filter_data_by_analysis_type_yearly():
    # Mock dataframes
    dummy_pnl_df = get_dummy_data()
    # Call the method under test
    filtered_data = filter_data_by_analysis_type(dummy_pnl_df, "2019-01-01", "yearly")

    # Assert the result
    assert len(filtered_data) > 0

    assert filtered_data['Cost_of_Sales'].sum() == 548588.7243079973

def test_filter_data_by_analysis_type_invalid_analysis_type():
    # Mock dataframe
    mock_df = MagicMock()

    # Call the method under test and assert it raises a ValueError
    with pytest.raises(ValueError):
        filter_data_by_analysis_type(mock_df, "2022-01-01", "invalid_type")

if __name__ == "__main__":
    pytest.main()
