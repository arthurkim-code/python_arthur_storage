import pandas as pd
import numpy as np

#df = pd.read_excel('CAR_test.xlsx')
excel_url = 'POA1.xlsx'

df1 = pd.read_excel(excel_url, sheet_name = "Team",  skiprows=[0]).set_index(["의사 Onekey ID", "담당자", "Territory"])
df2 = df1.iloc[:10,0:10]

df2 = df2.stack().reset_index()
df2.columns=['의사원키','담당자','영역','제품','목표']


#df3 = df2.iloc[:,]
#df3 = pd.merge(df1, df2[['Account: OneKeyId','Account: Account Name']], on='Account: OneKeyId', how='left')
#print(df2.head())

#print(df2.head(13))
#print(df2.head())WKP_USUAL_NAME


#df3 = df2.pivot_table(value="TFL-F",index="의사", columns="")

#df2 = df2.loc[:, (df2 != 0.0).any(axis=0)]

df2=df2[df2.목표 !=0.0]
#df2 = df3.drop_duplicates()

#print(df2.columns)

df2.to_excel('unpivot.xlsx', index=False)

