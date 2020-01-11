# important first import pandas and numpy
import pandas as pd
import numpy as np

# To connect with daba base
from sqlalchemy import create_engine

# Create connection
sqlitedb_path = './data/raw/emiliopatio.db'
engine = create_engine(f'sqlite:///{sqlitedb_path}')

# list all tables in database
pd.read_sql_query("SELECT * FROM sqlite_master WHERE type='table'", engine)

# 1. Read tables and go to dataframe
# 2. Merge personal and business dataframes
# 3. Merge personal,business and rank dataframes
# 4. Call to function

def acquire(path):
    business = pd.read_sql_query("SELECT * FROM business_info", engine)
    personal = pd.read_sql_query("SELECT * FROM personal_info", engine)
    rank = pd.read_sql_query("SELECT * FROM rank_info", engine)
    rank = rank.dropna()
    df_merge_personal_and_business = pd.merge(personal, business, on='id')
    df_all = pd.merge(df_merge_personal_and_business, rank, on='id')
    return df_all

def save_table(df,file_name):
    df.to_csv('./data/processed/{}.csv'.format(file_name))

def adquire_new_df(url):
    dfs = pd.read_html(url)
    data_new = dfs[11]
    data_new.to_csv('./data/processed/data_1_new_to_process.csv')
    return data_new


"""def adquire_new_df(url, year):
    dfs = pd.read_html(url)


    if year == 2010:
        data_new = dfs[11]

    elif year == 2011:
        data_new = dfs[10]

    elif year == 2012:
        data_new = dfs[9]

    elif year == 2013:
        data_new = dfs[8]

    elif year == 2014:
        data_new = dfs[7]

    elif year == 2015:
        data_new = dfs[6]

    elif year == 2016:
        data_new = dfs[5]

    elif year == 2017:
        data_new = dfs[4]

    else:
        raise ValueError('Value not admited')"""

"""data_new.to_csv('./data/processed/data_1_new_to_process.csv')"""








