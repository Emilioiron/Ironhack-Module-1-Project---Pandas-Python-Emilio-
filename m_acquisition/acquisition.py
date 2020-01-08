# important first import pandas and numpy
import pandas as pd
import numpy as np

# To connect with daba base
from sqlalchemy import create_engine
from sqlalchemy import exc
from sqlalchemy import event
from sqlalchemy import select

# Create connection
sqlitedb_path = './data/raw/emiliopatio.db'
engine = create_engine(f'sqlite:///{sqlitedb_path}')

# list all tables in database
pd.read_sql_query("SELECT * FROM sqlite_master WHERE type='table'", engine)

# 1. Read tables and go to dataframe
# 2. Merge personal and business dataframes
# 3. Merge personal,business and rank dataframes
# 4. Call to function

path = './data/raw/emiliopatio.db'

def acquire(path):
    business = pd.read_sql_query("SELECT * FROM business_info", engine)
    personal = pd.read_sql_query("SELECT * FROM personal_info", engine)
    rank = pd.read_sql_query("SELECT * FROM rank_info", engine)
    
    # remove null values from column "position" df range 
    # since if it does not give warning of the type SettingwithCopyWarning
    rank = rank.dropna()
    df_merge_personal_and_business = pd.merge(personal, business, on='id')
    df_all = pd.merge(df_merge_personal_and_business, rank, on='id')
    return df_all
df_all = acquire(path)

# Save all tables to CSV file
def save_table(df):
    df_all.to_csv('./data/processed/df_all.csv')
    return
# hasta aquí meterlo en un adquisition.py

def acquisition(path):
    df_all = acquire(path)
    save_table(df_all)
    return df_all
df_all = acquisition(path)




