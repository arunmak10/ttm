import pandas as pd
from faker import Faker

def gen_fake_wcf(size=1000):
    fake = Faker()
    working_capital_data = pd.DataFrame({
        'Date': pd.date_range(start='1950-01-31', periods=size),
        'Inventory': [fake.random_number(digits=5) for _ in range(size)],
        'Accounts_Receivable': [fake.random_number(digits=5) for _ in range(size)],
        'Accounts_Payable': [fake.random_number(digits=5) for _ in range(size)]
    })
    return working_capital_data

def gen_fake_pnl(size=1000):
    fake = Faker()
    pnl_data = pd.DataFrame({
        'Date': pd.date_range(start='1950-01-31', periods=size),
        'Sales': [fake.random_number(digits=5) for _ in range(size)],
        'Cost_of_Sales': [fake.random_number(digits=5) for _ in range(size)],
        'Net_Income': [fake.random_number(digits=5) for _ in range(size)],
        'Depreciation': [fake.random_number(digits=5) for _ in range(size)]
    })
    return pnl_data


