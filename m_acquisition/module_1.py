# 1. Read tables and go to dataframe
# 2. Merge personal and business dataframes
# 3. Merge personal,business and rank dataframes
# 4. Call to function


def init_table():
    business = pd.read_sql_query("SELECT * FROM business_info", engine)
    personal = pd.read_sql_query("SELECT * FROM personal_info", engine)
    rank = pd.read_sql_query("SELECT * FROM rank_info", engine)
    
    # remove null values from column "position" df range 
    # since if it does not give warning of the type SettingwithCopyWarning
    
    rank = rank.dropna()
    df_merge_personal_and_business = pd.merge(personal, business, on='id')
    df_all = pd.merge(df_merge_personal_and_business, rank, on='id')
    return df_all


# Save all tables to CSV file
def save_table(df):
    
    df_all.to_csv('../data/processed/df_all.csv')
    return 
# hasta aquí meterlo en un adquisition.py

def delete_columns(df):
    # define valid columns
    valid_columns = ['id', 'age','worth','lastName', 'position']
    # create new df with valid columns
    data = df[[x for x in df.columns if x in valid_columns]]
    
    return data


# Remove column text
# See the WARNING in https://www.dataquest.io/blog/settingwithcopywarning/
def replace_text(df):
    df.loc[:,'worth'] = df['worth'].str.replace('BUSD', '')
    df.loc[:,'age'] = df['age'].str.replace('years old', '')
    df.rename(columns={'worth': 'worth 2019 in BUSD'}, inplace = True)
    return data


# text
def lower_text(df):
    df['lastName'] = df['lastName'].apply(lambda x: x.lower())
    return data



def change_column_type(df):
    object_column = list(df.loc[:, df.dtypes == np.object])
    
    for i in object_column:
        if i != 'lastName':
            df[i] = pd.to_numeric(df[i])
        
    return data


# Save first clean table to CSV file
def save_table(df):
    
    data.to_csv('../data/processed/data.csv')
    

def wrangling(df):
    df2=delete_columns(df)
    df3=replace_text(df2)

hasta aquí meterlo en un punto


