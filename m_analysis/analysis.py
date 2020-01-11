import pandas as pd
import numpy as np
import requests
import html5lib
import matplotlib
import matplotlib.pyplot as plt



def wealth_difference(df):
    df['difference_19_10']= df['worth_2019_in_BUSD']- df['worth 2010 in BUSD']
    df_final_2 = df
    return df_final_2

