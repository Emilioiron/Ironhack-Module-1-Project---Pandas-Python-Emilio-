# important first import pandas and numpy
import pandas as pd
import numpy as np
from m_acquisition import acquisition as acq
from m_wrangling import wrangling as wr
from m_analysis import analysis as an
from m_reporting import reporting as rp


path = './data/raw/emiliopatio.db'
url = 'https://en.wikipedia.org/wiki/The_World%27s_Billionaires'
year = int(input('Indica un año entre 2017 y 2010:'))
title = input('title:')

if __name__ == '__main__':
    print('Ejecutando como programa principal')
    df_all = acq.acquire(path)                       ######## acquisition df_all
    data_new = acq.adquire_new_df(url)
    acq.save_table(df_all, 'df_all')
    df_2 = wr.delete_columns_1(df_all)               ######## wrangling
    df_3 = wr.replace_text(df_2)
    df_4 = wr.lower_text(df_3)
    data = wr.change_column_type(df_4)
    wr.save_table_1(data)
                                                        ###### acquisition df_final
    """data_new = wr.adquire_new_df(url)"""
    data_aux = wr.delete_columns_2(data_new)
    df_final = wr.final_table(data, data_aux)
    wr.save_table_2(df_final)
                                                         #########Analysis
    df_final_2 = an.wealth_difference(df_final)
                                                         ######### Reporting
    barchart = rp.visualize(df_final, title)
    rp.save_barchart(barchart)


