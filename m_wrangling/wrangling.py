# important first import pandas and numpy
import pandas as pd
import numpy as np
from m_acquisition import acquisition


path = './data/raw/emiliopatio.db'
df_all = acquisition.acquisition(path)

def delete_columns(df):
    # define valid columns
    valid_columns = ['id', 'age', 'worth', 'lastName', 'position']
    # create new df with valid columns
    df_2 = df[[x for x in df.columns if x in valid_columns]]
    return df_2
df_2 = delete_columns(df_all)

# Remove column text
# See the WARNING in https://www.dataquest.io/blog/settingwithcopywarning/
def replace_text(df):
    df.loc[:, 'worth'] = df['worth'].str.replace('BUSD', '')
    df.loc[:, 'age'] = df['age'].str.replace('years old', '')
    df.rename(columns={'worth': 'worth_2019_in_BUSD'}, inplace=True)
    df_3 = df
    return df_3
df_3 = replace_text(df_2)

# text
def lower_text(df):
    df['lastName'] = df['lastName'].apply(lambda x: x.lower())
    df_4 = df
    return df_4
df_4 = lower_text(df_3)

def change_column_type(df):
    data = df
    object_column = list(df.loc[:, df.dtypes == np.object])
    for i in object_column:
        if i != 'lastName':
            df[i] = pd.to_numeric(df[i])
    return data
data = change_column_type(df_4)
# Save first clean table to CSV file
def save_table(df):
    data.to_csv('./data/processed/data.csv')

def wrangling(df_all):
    df_2 = delete_columns(df_all)
    df_3 = replace_text(df_2)
    df_4 = lower_text(df_3)
    data = change_column_type(df_4)
    save_table(data)
    return data
data = wrangling(df_all)

