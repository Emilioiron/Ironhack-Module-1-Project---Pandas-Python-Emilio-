import pandas as pd
import numpy as np
from m_wrangling import wrangling
import requests
import html5lib
import matplotlib
import matplotlib.pyplot as plt
from m_acquisition import acquisition
from m_analysis import analysis


path = './data/raw/emiliopatio.db'
df_all = acquisition.acquisition(path)
data = wrangling.wrangling(df_all)
url = 'https://en.wikipedia.org/wiki/The_World%27s_Billionaires'

def adquire_new_df(url):
    dfs = pd.read_html(url)
    return dfs
dfs = adquire_new_df(url)

"""
def adquire_init_df():
    data = pd.read_csv("./data/processed/data.csv", index_col=0)
    return data
data = adquire_init_df()
"""

year = input('Indica un año entre 2017 y 2010:')

def select_year(str):
    data_year = str
    error = 'ValueError'
    if data_year == '2010':
        data_new = dfs[11]
        return data_new
    elif data_year == '2011':
        data_new = dfs[10]
        return data_new
    elif data_year == '2012':
        data_new = dfs[9]
        return data_new
    elif data_year == '2013':
        data_new = dfs[8]
        return data_new
    elif data_year == '2014':
        data_new = dfs[7]
        return data_new
    elif data_year == '2015':
        data_new = dfs[6]
        return data_new
    elif data_year == '2016':
        data_new = dfs[5]
        return data_new
    elif data_year == '2017':
        data_new = dfs[4]
        return data_new
    else:
        raise ValueError('Value not admited')
 
data_new = select_year(year)

def delete_columns(df):
    # define valid columns
    valid_columns = ['Name', 'Net worth (USD)']
    # create new df with valid columns
    data_new1 = df[[x for x in df.columns if x in valid_columns]]
    return data_new1

data_new1 = delete_columns(data_new)

def replace_text(df):
    df.loc[:,'Net worth (USD)'] = df['Net worth (USD)'].str.replace('billion', '')
    df.loc[:,'Net worth (USD)'] = df['Net worth (USD)'].str.replace('$', '')
    df.loc[:,'Name'] = df['Name'].str.replace('& family', '')
    data_new2 = df.rename(columns={'Net worth (USD)': 'worth 2010 in BUSD'}, inplace = True)
    return data_new2
data_new2 = replace_text(data_new1)

def auxiliar_df(df):
    new = df['Name'].str.split(' ', n = 1, expand = True)
    return new
new = auxiliar_df(data_new2)

def split_column(df,new):
    # making separate last name column from new data frame
    df['lastName']= new[1]
    # Dropping old Name columns
    df.drop(columns =['Name'], inplace = True)
    data_new3 = df
    return data_new3
data_new3 = split_column(data_new2,)

def lower_text(df):
    df['lastName'] = df['lastName'].apply(lambda x: x.lower())
    data_new4 = df
    return data_new4
data_new4 = lower_text(data_new3)

def change_column_type_2(df):
    df['worth 2010 in BUSD'] = df['worth 2010 in BUSD'].astype(float)
    data_new5 = df
    return data_new5
data_new5 = change_column_type_2(data_new4)

def final_table(df1,df2):
    data_new6 = pd.merge(df1, df2, on='lastName')
    df_final = data_new6.drop_duplicates(subset='lastName', keep='first')
    return df_final
df_final = final_table(data, data_new5)


#Save_table(df_final)

def wealth_difference(df):
    df_final['difference_19_10']= df_final['worth 2019 in BUSD']-df_final['worth 2010 in BUSD']
    df_final_difference = df_final
    return df_final_difference
df_final_difference = wealth_difference(df_final)

# Save first clean table to CSV file
def save_table(df):
    df_final.to_csv('./data/processed/df_final_difference.csv')

def analysis(data):
    dfs = adquire_new_df(url)
    # data = adquire_init_df()
    data_new = select_year(year)
    data_new1 = delete_columns(data_new)
    data_new2 = replace_text(data_new1)
    data_new3 = split_column(data_new2)
    new = auxiliar_df(data_new2)
    data_new4 = lower_text(data_new3)
    data_new5 = change_column_type_2(data_new4)
    df_final = final_table(data, data_new5)
    df_final_difference = wealth_difference(df_final)
    save_table(df_final_difference)
    return df_final_difference
df_final_difference = analysis(data)
