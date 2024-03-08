import pytest
from fastapi.testclient import TestClient
from backend.main import app
from unittest.mock import patch
from fastapi import HTTPException

client = TestClient(app)

def test_calculate_cash_flow_endpoint_missing_start_date():
    response = client.get("/cash-flow/?analysis_type=monthly")
    assert response.status_code == 422
    

def test_calculate_cash_flow_endpoint():
    response = client.get("/cash-flow/?analysis_type=monthly&start_date=2019-01-01")
    assert response.status_code == 200
    assert "cash_flow" in response.json()

def test_calculate_cash_flow_endpoint_with_additional_info():
    response = client.get("/cash-flow/?analysis_type=monthly&start_date=2019-01-01&more_info=True")
    assert response.status_code == 200
    assert "cash_flow" in response.json()
    assert "additional_info" in response.json()

if __name__ == "__main__":
    pytest.main()