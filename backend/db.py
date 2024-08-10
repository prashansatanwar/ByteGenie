from sqlalchemy import create_engine, text
from data import get_company_data, get_event_data, get_people_data

import os
from dotenv import load_dotenv

load_dotenv()

username = os.environ.get('DB_USERNAME')
password = os.environ.get('DB_PASSWORD')
host = os.environ.get('DB_HOST')
port = os.environ.get('DB_PORT')

DATABASE = 'ByteGenie'

COMPANY_SCHEMA = """
  company_logo_url VARCHAR(255),
  company_logo_text VARCHAR(255),
  company_name VARCHAR(255),
  relation_to_event VARCHAR(255),
  event_url VARCHAR(255),
  company_revenue DOUBLE,
  n_employees INT,
  company_phone VARCHAR(255),
  company_founding_year VARCHAR(4),
  company_address VARCHAR(255),
  company_industry VARCHAR(255),
  company_overview TEXT,
  homepage_url VARCHAR(255),
  linkedin_company_url VARCHAR(255),
  homepage_base_url VARCHAR(255),
  company_logo_url_on_event_page VARCHAR(255),
  company_logo_match_flag VARCHAR(255)
"""

EVENT_SCHEMA = """
  event_logo_url VARCHAR(255),
  event_name VARCHAR(255),
  event_start_date DATE,
  event_end_date DATE,
  event_venue VARCHAR(255),
  event_country VARCHAR(255),
  event_description TEXT,
  event_url VARCHAR(255)
"""

PEOPLE_SCHEMA = """
  first_name VARCHAR(255),
  middle_name VARCHAR(255),
  last_name VARCHAR(255),
  job_title VARCHAR(255),
  person_city VARCHAR(255),
  person_state VARCHAR(255),
  person_country VARCHAR(255),
  email_pattern VARCHAR(255),
  homepage_base_url VARCHAR(255),
  duration_in_current_job TEXT,  
  duration_in_current_company TEXT  
"""

def init_db(username, password, host, port):
    # Create an engine for your MySQL database
    engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}')

    # Create database if it doesn't exist
    with engine.connect() as connection:
        try:
            connection.execute(text(f"USE {DATABASE};"))
        except:
            connection.execute(text(f"CREATE DATABASE {DATABASE};"))
            connection.execute(text(f"USE {DATABASE};"))

    # Reconnect to the specific database
    engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{DATABASE}')

    return engine

def populate_db(engine):
    with engine.connect() as connection:
      connection.execute(text(f"CREATE TABLE IF NOT EXISTS companies ("+COMPANY_SCHEMA+");"))
      connection.execute(text(f"CREATE TABLE IF NOT EXISTS events ("+EVENT_SCHEMA+");"))
      connection.execute(text(f"CREATE TABLE IF NOT EXISTS people ("+PEOPLE_SCHEMA+");"))

    get_company_data().to_sql('companies', engine, if_exists='append', index=False)
    get_event_data().to_sql('events', engine, if_exists='append', index=False)
    get_people_data().to_sql('people', engine, if_exists='append', index=False)
    

def get_db_engine(username, password, host, port):
    engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{DATABASE}')
    return engine
    
def execute_query(query):
  engine = get_db_engine(username,password,host,port)
  with engine.connect() as connection:
      result = connection.execute(text(query))

      output =  {
          "column_names": list(result.keys()),
          "data": [list(row) for row in result]
      }

      return output
  

if __name__ == '__main__':
  engine = init_db(username,password,host,port)
  populate_db(engine)