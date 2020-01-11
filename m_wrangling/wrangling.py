# important first import pandas and numpy
import pandas as pd
import numpy as np



path = './data/raw/emiliopatio.db'
url = 'https://en.wikipedia.org/wiki/The_World%27s_Billionaires'

def delete_columns_1(df):
    # define valid columns
    valid_columns = ['id', 'age', 'worth', 'lastName', 'position']
    # create new df with valid columns
    df_2 = df[[x for x in df.columns if x in valid_columns]]
    return df_2

# Remove column text
# See the WARNING in https://www.dataquest.io/blog/settingwithcopywarning/
def replace_text(df):
    df.loc[:, 'worth'] = df['worth'].str.replace('BUSD', '')
    df.loc[:, 'age'] = df['age'].str.replace('years old', '')
    df.rename(columns={'worth': 'worth_2019_in_BUSD'}, inplace=True)
    df_3 = df
    return df_3

# text
def lower_text(df):
    df['lastName'] = df['lastName'].apply(lambda x: x.lower())
    df_4 = df
    return df_4

def change_column_type(df):
    object_column = list(df.loc[:, df.dtypes == np.object])
    for i in object_column:
        if i != 'lastName':
            df[i] = pd.to_numeric(df[i])
    data = df
    return data


# Save first clean table to CSV file
def save_table_1(df):
    df.to_csv('./data/processed/data.csv')


def delete_columns_2(df):
    # define valid columns
    valid_columns = ['Name', 'Net worth (USD)']
    # create new df with valid columns
    df = df[[x for x in df.columns if x in valid_columns]]
    df.rename(columns={'Net worth (USD)': 'Net_worth_(USD)'}, inplace=True)
    df.loc[:,'Net_worth_(USD)'] = df['Net_worth_(USD)'].str.replace('billion', '')
    df.loc[:,'Net_worth_(USD)'] = df['Net_worth_(USD)'].str.replace('$', '')
    df.loc[:,'Name'] = df['Name'].str.replace(' & family', '')
    df.loc[:, 'Name'] = df['Name'].str.replace(' ', '_')
    df.rename(columns={'Net_worth_(USD)': 'worth 2010 in BUSD'}, inplace = True)
    name_list = df['Name'].tolist()
    list_lastName = [i.split('_', 1)[1] for i in name_list]
    df['new_column'] = pd.Series(list_lastName).values
    df.drop('Name', axis=1, inplace=True)
    df.rename(columns={'new_column': 'lastName'}, inplace = True)
    df['lastName'] = df['lastName'].apply(lambda x: x.lower())
    df['worth 2010 in BUSD'] = df['worth 2010 in BUSD'].astype(float)
    data_aux = df
    return data_aux


def final_table(df1,df2):
    df = pd.merge(df1, df2, on='lastName')
    df_final = df.drop_duplicates(subset='lastName', keep='first')
    return df_final


# Save first clean table to CSV file
def save_table_2(df):
    df.to_csv('./data/processed/df_final.csv')





