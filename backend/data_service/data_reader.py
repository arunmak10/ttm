# data_reader.py

import pandas as pd
from fastapi import HTTPException
from backend.config.constants import Constants

def read_working_capital_data(filename: str = None):
    if filename is None:
        filename = Constants.get_working_capital_file()
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"{filename} file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading {filename}: {str(e)}")

def read_pnl_data(filename: str = None):
    if filename is None:
        filename = Constants.get_pnl_file()
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"{filename} file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading {filename}: {str(e)}")
