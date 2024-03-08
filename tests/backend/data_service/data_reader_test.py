import pytest
from unittest.mock import patch
from backend.data_service.data_reader import read_working_capital_data, read_pnl_data
from fastapi import HTTPException
import pandas as pd

# Mock data
MOCK_WORKING_CAPITAL_FILE = "mock_working_capital.csv"
MOCK_PNL_FILE = "mock_pnl.csv"

@pytest.fixture
def mock_pd_read_csv():
    with patch('backend.data_service.data_reader.pd.read_csv') as mock_read_csv:
        yield mock_read_csv

@pytest.fixture
def mock_constants_get_working_capital_file():
    with patch('backend.data_service.data_reader.Constants.get_working_capital_file') as mock_get_wc_file:
        mock_get_wc_file.return_value = MOCK_WORKING_CAPITAL_FILE
        yield mock_get_wc_file

@pytest.fixture
def mock_constants_get_pnl_file():
    with patch('backend.data_service.data_reader.Constants.get_pnl_file') as mock_get_pnl_file:
        mock_get_pnl_file.return_value = MOCK_PNL_FILE
        yield mock_get_pnl_file

def test_read_working_capital_data_file_not_found(mock_pd_read_csv, mock_constants_get_working_capital_file):
    # Mock pd.read_csv to raise FileNotFoundError
    mock_pd_read_csv.side_effect = FileNotFoundError

    # Assert HTTPException is raised with status_code 404
    with pytest.raises(HTTPException) as exc_info:
        read_working_capital_data()
    assert exc_info.value.status_code == 404

def test_read_working_capital_data_general_error(mock_pd_read_csv, mock_constants_get_working_capital_file):
    # Mock pd.read_csv to raise a general error
    mock_pd_read_csv.side_effect = Exception("General error")

    # Assert HTTPException is raised with status_code 500
    with pytest.raises(HTTPException) as exc_info:
        read_working_capital_data()
    assert exc_info.value.status_code == 500

def test_read_working_capital_data_success(mock_pd_read_csv, mock_constants_get_working_capital_file):
    # Mock pd.read_csv to return a DataFrame
    mock_pd_read_csv.return_value = pd.DataFrame({'Date': ['2022-01-01'], 'Inventory': [100]})

    # Read data
    df = read_working_capital_data()

    # Assert the DataFrame is not empty
    assert not df.empty
    # Additional assertions as needed


@pytest.fixture
def mock_constants_get_pnl_file():
    with patch('backend.data_service.data_reader.Constants.get_pnl_file') as mock_get_pnl_file:
        mock_get_pnl_file.return_value = MOCK_PNL_FILE
        yield mock_get_pnl_file

def test_read_pnl_data_file_not_found(mock_pd_read_csv, mock_constants_get_pnl_file):
    # Mock pd.read_csv to raise FileNotFoundError
    mock_pd_read_csv.side_effect = FileNotFoundError

    # Assert HTTPException is raised with status_code 404
    with pytest.raises(HTTPException) as exc_info:
        read_pnl_data()
    assert exc_info.value.status_code == 404

def test_read_pnl_data_general_error(mock_pd_read_csv, mock_constants_get_pnl_file):
    # Mock pd.read_csv to raise a general error
    mock_pd_read_csv.side_effect = Exception("General error")

    # Assert HTTPException is raised with status_code 500
    with pytest.raises(HTTPException) as exc_info:
        read_pnl_data()
    assert exc_info.value.status_code == 500

def test_read_pnl_data_success(mock_pd_read_csv, mock_constants_get_pnl_file):
    # Mock pd.read_csv to return a DataFrame
    mock_pd_read_csv.return_value = pd.DataFrame({'Date': ['2022-01-01'], 'Sales': [100]})

    # Read data
    df = read_pnl_data()

    # Assert the DataFrame is not empty
    assert not df.empty
    


if __name__ == "__main__":
    pytest.main()
