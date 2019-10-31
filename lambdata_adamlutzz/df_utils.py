import numpy as np
import pandas as pd

def check_nulls(df):
    '''Pass in dataframe to chech for null values'''
    na_df = df.isna().sum()

    print('Null Values for Features\n')
    print(na_df)
