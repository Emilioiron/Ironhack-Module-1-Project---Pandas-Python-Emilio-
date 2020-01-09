# important first import pandas and numpy
import pandas as pd
import numpy as np
from m_acquisition import acquisition
from m_wrangling import wrangling
from m_analysis import analysis

path = './data/raw/emiliopatio.db'




if __name__ == '__main__':
    print('Ejecutando como programa principal')
    df_all = acquisition.acquire(path)
    save_table(df_all, 'df_all')
"""    data = wrangling.deleted_columns(df_all)

    df_final_difference = analysis.analysis(data)"""