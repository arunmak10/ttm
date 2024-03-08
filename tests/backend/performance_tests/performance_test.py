import pytest
import pandas as pd
import asyncio
from aiohttp import ClientSession
import time
from fake_data_gen import gen_fake_wcf, gen_fake_pnl
#from backend.config.constants import Constants
from faker import Faker

async def make_request(url, params):
    async with ClientSession() as session:
        start_time = time.time()
        async with session.get(url, params=params) as response:
            end_time = time.time()
            response_time = end_time - start_time
            return await response.json(), response_time

@pytest.mark.asyncio
async def test_performance(size=20):
    print(f"=============Performing some app performance for {size} number of concurrent requests ==========================================")
    url = "http://localhost:8000/cash-flow/"
    params = {
        "analysis_type": "monthly",
        "start_date": "2019-01-01",
        "more_info": "True"
    }
    #performance_test_with_inc_data()
    tasks = []
    for _ in range(size):  # Simulate default=10 time concurrent requests, adjust as needed
        task = asyncio.create_task(make_request(url, params))
        tasks.append(task)
    responses = await asyncio.gather(*tasks)
    
    # Extract response times from responses
    response_times = [response[1] for response in responses]
    
    # Perform analysis on response times
    total_response_time = sum(response_times)
    average_response_time = total_response_time / len(response_times)
    max_response_time = max(response_times)
    
    # Print performance metrics
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    print(f"Total response time: {total_response_time} seconds")
    print(f"Average response time: {average_response_time} seconds")
    print(f"Max response time: {max_response_time} seconds\n")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(f"=============Performance analysis completed for {size} number of concurrent requests==========================================")
    #restore_file()


""" def store_this_data( file_dict_info ):
    wcf_working_path = Constants.get_working_capital_file()
    pnl_working_path = Constants.get_working_capital_file()
    replace wcf_working_path with temp_wcf_working_path
    replace pnl_working_path with temp_pnl_working_path
    store file_dict_info['working_capital.csv'] at wcf_working_path
    store file_dict_info['pnl.csv'] at pnl_working_path


def perfomance_test_with_inc_data():
    wcf = gen_fake_wcf(1000)
    pnl = gen_fake_pnl(1000)
    filename_data_dict = { 'working_capital.csv' : wcf, 'pnl.csv': pnl }
    store_this_data(filename_data_dict)
    
def complete_performance_test():
    wcf = gen_fake_wcf(1000)
    pnl = gen_fake_pnl(1000)
    filename_data_dict = { 'working_capital.csv' : wcf, 'pnl.csv': pnl }
    store_this_data(filename_data_dict) """

""" 
import os

def rename_file(original_path):
    # Extract directory and filename from the original path
    directory, filename = os.path.split(original_path)
    
    # Construct the new filename with "temp_" prefix
    new_filename = "temp_" + filename
    
    # Construct the new path with the renamed filename
    new_path = os.path.join(directory, new_filename)
    
    # Rename the file
    os.rename(original_path, new_path)
    
    return new_path

def restore_file():
    og_wcf_working_path = Constants.get_working_capital_file()
    og_pnl_working_path = Constants.get_working_capital_file()

    temp_wcf_working_path = og_wcf_working_path.replace("working_capital.csv", "temp_working_capital.csv")
    temp_pnl_working_path = og_pnl_working_path.replace("pnl.csv", "temp_pnl.csv")

    #replacing original filename to temp_filename.csv for testing
    og_wcf_df = pd.read_csv(temp_wcf_working_path)
    og_wcf_df.to_csv(og_wcf_working_path)
    og_pnl_df = pd.read_csv(temp_pnl_working_path)
    og_pnl_df.to_csv(og_pnl_working_path)

# Example usage 
""" """ original_file_path = "/path/filename.csv"
new_file_path = rename_file(original_file_path)
print("File renamed to:", new_file_path) """
"""


def store_this_data(file_dict_info):
    og_wcf_working_path = Constants.get_working_capital_file()
    og_pnl_working_path = Constants.get_pnl_file()

    temp_wcf_working_path = og_wcf_working_path.replace("working_capital.csv", "temp_working_capital.csv")
    temp_pnl_working_path = og_pnl_working_path.replace("pnl.csv", "temp_pnl.csv")

    #replacing original filename to temp_filename.csv for testing
    og_wcf_df = pd.read_csv(og_wcf_working_path)
    og_wcf_df.to_csv(temp_wcf_working_path)
    og_pnl_df = pd.read_csv(og_pnl_working_path)
    og_pnl_df.to_csv(temp_pnl_working_path)
    #replace the original to temp_filename.csv to test performance with large data set
    #_, wdf_file = os.path.split(og_wcf_working_path)
    #directory, pnl_file = os.path.split(og_pnl_working_path)
    
   
    
    file_dict_info['working_capital.csv'].to_csv(og_wcf_working_path)
    file_dict_info['pnl.csv'].to_csv(og_pnl_working_path)

def gen_fake_wcf(size=1000):
    fake = Faker()
    working_capital_data = pd.DataFrame({
        'Date': pd.date_range(start='1950-01-01', periods=size),
        'Inventory': [fake.random_number(digits=5) for _ in range(size)],
        'Accounts_Receivable': [fake.random_number(digits=5) for _ in range(size)],
        'Accounts_Payable': [fake.random_number(digits=5) for _ in range(size)]
    })
    return working_capital_data

def gen_fake_pnl(size=1000):
    fake = Faker()
    pnl_data = pd.DataFrame({
        'Date': pd.date_range(start='1950-01-01', periods=size),
        'Sales': [fake.random_number(digits=5) for _ in range(size)],
        'Cost_of_Sales': [fake.random_number(digits=5) for _ in range(size)],
        'Net_Income': [fake.random_number(digits=5) for _ in range(size)],
        'Depreciation': [fake.random_number(digits=5) for _ in range(size)]
    })
    return pnl_data

def performance_test_with_inc_data():
    wcf = gen_fake_wcf(1000)
    pnl = gen_fake_pnl(1000)
    filename_data_dict = {'working_capital.csv': wcf, 'pnl.csv': pnl}
    store_this_data(filename_data_dict)
    #test_performance()
    
def complete_performance_test():
    wcf = gen_fake_wcf(1000)
    pnl = gen_fake_pnl(1000)
    filename_data_dict = {'working_capital.csv': wcf, 'pnl.csv': pnl}
    store_this_data(filename_data_dict)

    
"""