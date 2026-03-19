# db_connect.py

import psycopg2
import os
import creds as creds 
import pandas as pd
from sqlalchemy import create_engine

CSV_PATH = 'wrs_results.csv' 
PG_TABLE_NAME = 'results'
DB_HOST = 'localhost' # or 'postgres_service_name' 
DB_PORT = '5432'
DB_NAME = 'wrs_data'
DB_USER = 'admin'
DB_PASSWORD = creds.db_password # or use os.environ['DB_PASSWORD']

CONN_STRING = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(CONN_STRING)


def connect_to_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

# CONN = connect_to_db()

def create_table(df):
    pass

def csv_to_db():
    df = pd.read_csv(CSV_PATH)
    df.astype(str)
    with engine.connect() as conn_test:
        df.to_sql(PG_TABLE_NAME, conn_test, if_exists='replace', index=False)



# Example Usage
if __name__ == "__main__":
    # connection = connect_to_db()

    csv_to_db()

    # if connection:
    #     cursor = connection.cursor()
    #     create_table = "CREATE TABLE if not exists results (id varchar, name varchar, result varchar, date varchar);"
    #     cursor.execute(create_table)
    #     connection.commit()
    #     check_contents = "select * from results;"
    #     # check_contents = "SELECT current_schema;;"
    #     cursor.execute(check_contents)
    #     records = cursor.fetchall()
    #     print(records)
    #     connection.close()