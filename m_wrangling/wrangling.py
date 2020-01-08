
def delete_columns(df):
    # define valid columns
    valid_columns = ['id', 'age', 'worth', 'lastName', 'position']
    # create new df with valid columns
    data = df[[x for x in df.columns if x in valid_columns]]
    return data
data = delete_columns(df)

# Remove column text
# See the WARNING in https://www.dataquest.io/blog/settingwithcopywarning/
def replace_text(df):
    df.loc[:, 'worth'] = df['worth'].str.replace('BUSD', '')
    df.loc[:, 'age'] = df['age'].str.replace('years old', '')
    df.rename(columns={'worth': 'worth 2019 in BUSD'}, inplace=True)
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
    df2 = delete_columns(df)
    df3 = replace_text(df2)

# hasta aquí meterlo en un punto
