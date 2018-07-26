#!/usr/bin/python
# -*- coding: utf-8 -*-

""" This is a simple python script that will calculate the f1 score
    for the dates that occur on Thursday.

    This script has been created as part of a request from Nearmap's job
    application process to demonstrate this candidate's attention to detail

    Please download the file provided by Nearmap and uncompress into
    the same directory as this python file.
"""

import pandas as pd
from sklearn.metrics import f1_score

__author__ = "Calan Holmes"
__date__ = "2018-07-24"
__version__ = "1.0.1"
__email__ = "calan.holmes@gmail.com"
__status__ = "Production"

df = pd.read_csv('test.psv', sep='|', header=1, skiprows=0, parse_dates=['dates'])

# note: Thursday = 3, as the index for date starts with Monday = 0
df_thursdays_only = df.loc[pd.to_datetime(df['dates']).dt.dayofweek == 3]

f1 = f1_score(df_thursdays_only['y'], df_thursdays_only['yhat'], average='macro')
print('{:.5f}'.format(f1))
