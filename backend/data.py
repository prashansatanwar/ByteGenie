import math
import pandas as pd

# averaging the number of employees
def convert_employees(x):
    if isinstance(x, str):
        x = x.replace(',', '') 
        if '+' in x:
            return int(x.replace('+', ''))  
        if 'employees' in x:
            x = x.replace('employees', '').strip()
        if '-' in x:
            low, high = x.split('-')
            return int(math.ceil((int(low) + int(high)) / 2)) 
        else:
            return int(math.ceil(float(x)))
        
# converting revenue to float
def convert_revenue(revenue):
    if isinstance(revenue, str):
        revenue = revenue.replace(',', '').strip()  
        if 'billion' in revenue:
            number = float(revenue.replace('$', '').replace('billion', '').strip())
            return number * 1_000_000_000.0
        elif 'million' in revenue:
            number = float(revenue.replace('$', '').replace('million', '').strip())
            return number * 1_000_000.0
        else:
            return float(revenue.replace('$', '').strip())  

# returns company data
def get_company_data():
    company_info = pd.read_csv("data/company_info.csv")
    ci_df = pd.DataFrame(company_info)

    ci_df = ci_df.dropna()

    ci_df['n_employees'] = ci_df['n_employees'].apply(convert_employees).astype('Int64')
    ci_df['company_revenue'] = ci_df['company_revenue'].apply(convert_revenue).astype('Float64')  

    return ci_df

# returns event data
def get_event_data():
    event_info = pd.read_csv("data/event_info.csv")
    ei_df = pd.DataFrame(event_info)

    return ei_df

# returns people data
def get_people_data():
    people_info = pd.read_csv("data/people_info.csv")
    pi_df = pd.DataFrame(people_info)

    return pi_df