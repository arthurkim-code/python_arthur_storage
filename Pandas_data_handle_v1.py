#Excel Pandas example_2201

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc('font', family='Malgun Gothic')
#df = pd.read_excel('CAR_test.xlsx')
excel_url = 'Data09.csv'
excel_to ='Resutl.csv'

df1 = pd.read_csv(excel_url, encoding='cp949')
print(df1.shape)

df2=pd.DataFrame(df1.drop(columns=['순번','상품코드']).set_index('상품명').stack()).reset_index()

region_list = df1.columns.to_list()[4:]

cond1=(df2['상품명'].isnull())
cond2=(df2['상품명'] !='합 계')
cond3=(df2['level_1'] !=' 합계')


df3=df2.loc[(~cond1)&(cond2)&(cond3)]
df4=df3.rename(columns={'level_1':'점포명',0:'수량'})

def func1(row):
    if 'CAT' in row:
        return "C TYPE"
    elif 'STL' in row:
        return "S TYPE"
    elif 'BW' in row:
        return "B TYPE"
    else:
        return "Non Type"


df4['제품군']=df4['상품명'].apply(func1)

cond1=df4['제품군'] != 'Non Type'
df5=df4.loc[(cond1)]

def func2(row):
    if len(row) >=4:
        result=row.split(',')
        return result[0] + result[1]
    else:
        return row


df5['수량(int)']=(df5['수량'].apply(func2)).astype(int)

#df6['수량'].astype(int)
#df5.info()

df6 = pd.pivot_table(data=df5,index=['점포명','제품군'], values='수량(int)', aggfunc='sum').reset_index()

df7 = df6.sort_values(by='수량(int)', ascending=False)

df7.to_csv(excel_to, encoding='cp949')

#print(df1.head(10))

#print(df4.head(10))
#print(df4['제품군'].value_counts())
#print(df3['상품명'].unique())


#df2 = df1.iloc[:10,0:10]

#df2 = df2.stack().reset_index()
#df2.columns=['의사원키','담당자','영역','제품','목표']


#df3 = df2.iloc[:,]
#df3 = pd.merge(df1, df2[['Account: OneKeyId','Account: Account Name']], on='Account: OneKeyId', how='left')
#print(df2.head())

#print(df2.head(13))
#print(df2.head())WKP_USUAL_NAME


#df3 = df2.pivot_table(value="TFL-F",index="의사", columns="")

#df2 = df2.loc[:, (df2 != 0.0).any(axis=0)]

#df2=df2[df2.목표 !=0.0]
#df2 = df3.drop_duplicates()

#print(df1.head())

#df2.to_excel('unpivot.xlsx', index=False)

