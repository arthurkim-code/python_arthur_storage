#Excel Pandas example_2202_ver1
#Drop Duplicate with latest date condition

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse
import arrow

mpl.rc('font', family='Malgun Gothic')
#df = pd.read_excel('CAR_test.xlsx')
excel_url = 'opt.xlsx'
excel_to ='drop_duplicate.xlsx'

#df1 = pd.read_excel(excel_url, skiprows=1)
df1 = pd.read_excel(excel_url, skiprows=20)
df2 = df1.drop(columns=['Unnamed: 0','Unnamed: 2'])

#df2['Date2'] = df2['Date1'].datetime.strftime("%m/%d/%Y %H:%M:%S")
df2['TimeStamp'] = pd.to_datetime(df2['Date1'], format="%Y. %m. %d %p %H:%M")
#df2['test'] = parse(df2.Date1)
'''
def func2(row):

   #row1=row.datetime.strftime("%m/%d/%Y %H:%M:%S")
   #row1=parser.parse(row).isoformat()
   row1=parse(row).datetime()
   return row1

df2['opt(date)']=df2['Date1'].apply(func2)
'''
#df2['Opt date[date]'] = pd.to_datetime(df2['Opt date'])


#df1['PW'] = 'sk' + df1['EmployeeNumber'].astype(str)
#df1['reset'] = "System.setPassword('" + df1['Id'] + "," + "'" + df1['PW']+ "'" + ");"
#df2 = df1['reset']

df3 = df2.sort_values(by=['TimeStamp'])
df3=df3.drop_duplicates(subset=['OneKeyId'], keep='last')

#df3 = df2.sort_values('TimeStamp').drop_duplicates('OnekeyId', keep='last')
#df3=df2.loc[df2.groupby('OnekeyId', sort=False)['TimeStamp'].idxmax()]

#print(df2.columns)
df3.to_excel(excel_to)