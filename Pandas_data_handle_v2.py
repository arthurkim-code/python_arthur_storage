#Excel Pandas example_2201_ver2

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc('font', family='Malgun Gothic')
#df = pd.read_excel('CAR_test.xlsx')
excel_url = 'Data05.xlsx'
excel_to ='Result_ver2.xlsx'

df1 = pd.read_excel(excel_url, skiprows=1)
df2=pd.DataFrame(df1.iloc[:,8:-2].stack()).reset_index().iloc[1:]

df3=df1.iloc[:,6:-2].drop(columns=['Unnamed: 7','판매']).set_index(['제품명']).stack().reset_index()
df4=pd.DataFrame(df3)
df5=df4.rename(columns={'level_1':'날짜',0:'재고량'})

df6=df1[['카테고리명','자재그룹','자재그룹명','제품코드','제품명',' 분류']]

df7=pd.merge(df6,df5,how='right',on='제품명')

#print(df2)
#print(df7)
df7['날짜(전처리)']=pd.to_datetime(df7['날짜'])
df7['공급월'] = df7['날짜(전처리)'].dt.month
#df7['공급'] = df7['날짜(전처리)'].dt.month
#f7['공급월'] = df7['날짜(전처리)'].dt.month
df7=pd.DataFrame(pd.pivot_table(data=df7,index='공급월',values='재고량',aggfunc='sum'))
sns.barplot(data=df7, x='공급월', y='재고량', ci=None, estimator=sum)
plt.savefig('img_result.png')
#print(sns)
#df7.to_excel(excel_to)

#df2=pd.DataFrame(df1.drop(columns=['순번','상품코드']).set_index('상품명').stack()).reset_index()