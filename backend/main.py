from fastapi import FastAPI, HTTPException
from backend.config.constants import Constants
from backend.data_service.data_reader import read_working_capital_data, read_pnl_data
from backend.data_service.data_filter import filter_data_by_analysis_type
from backend.calculator_service.cash_flow_calculator import calculate_cash_flow, calculate_additional_ratios

app = FastAPI()

@app.get("/cash-flow/")
async def calculate_cash_flow_endpoint(analysis_type: str, start_date: str, more_info=False):
    #Covered in default behavior of missing post params FASTApi()
    # Read working capital data
    working_capital_data = read_working_capital_data()

    # Read P&L data
    pnl_data = read_pnl_data()

    # Calculate cash flow
    try:
        cash_flow_result = calculate_cash_flow(pnl_data, working_capital_data, start_date, analysis_type)
        cash_flow_json = {
            "cash_flow": cash_flow_result,
        }
        if more_info=="True":
            additional_ratios = calculate_additional_ratios(pnl_data, working_capital_data, start_date, analysis_type)
            cash_flow_json["additional_info"] = additional_ratios
        
        return cash_flow_json
    except ValueError as e:
        # return an HTTP 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
