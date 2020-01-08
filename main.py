# important first import pandas and numpy
import pandas as pd
import numpy as np
from m_acquisition import module_1
from module_1 import * 


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

init_table()



if__name__ == '__main__':
    data = acquire()
    
