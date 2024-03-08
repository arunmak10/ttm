import os
import pytest
from unittest.mock import MagicMock, patch
from backend.config.constants import Constants


@pytest.fixture
def mock_config_parser():
    return MagicMock()

@pytest.fixture
def mock_config_instance(mock_config_parser):
    mock_config = MagicMock()
    mock_config['Paths'] = {'WorkingCapitalData': "/path/to/working_capital.csv",
                            'PNLData': "/path/to/pnl.csv"}
    mock_config_parser.return_value = mock_config
    return mock_config

#@MagicMock.mock_calls('Constants')
def test_get_working_capital_file(mock_config_parser):
    with patch('backend.config.constants.Constants.get_working_capital_file') as mock_get_working_capital_file:
        # Set the return value of the mocked method
        mock_get_working_capital_file.return_value = "/path/to/working_capital.csv"
        working_capital_file = Constants.get_working_capital_file()
        assert working_capital_file == "/path/to/working_capital.csv"
        


def test_get_pnl_file(mock_config_parser):
    with patch('backend.config.constants.Constants.get_pnl_file') as mock_get_pnl_file:
        # Set the return value of the mocked method
        mock_get_pnl_file.return_value = "/path/to/pnl.csv"
        pnl_file = Constants.get_pnl_file()
        assert pnl_file == "/path/to/pnl.csv"
        

if __name__ == "__main__":
    pytest.main()
