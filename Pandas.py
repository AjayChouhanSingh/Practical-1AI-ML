import numpy as np
import pandas as pd
arr=np.array([1,2,3,4,np.nan,6,7])
print(arr)
s=pd.Series(arr)
print(s)
print('-'*30)
dates=pd.date_range(start='20191202',periods=5)
print(dates)
print('-'*30)
datesDF=pd.DataFrame(np.random.randn(5,5),index=dates,columns=list('ABCDE'))
print(datesDF)
print('-'*30)
dict1={
       'Name':['Ajay','Luv','Jhanvi','Tushar','Anil'],
       'Age':[21,20,21,21,21],
       'Gender':['Male','Male','Female','Male','Male'],
       'Job':['Student','Student','Student','Student','Student']
       }
df2=pd.DataFrame(dict1,index=list('ABCDE'))
print(df2)
print('-'*30)
print(df2.dtypes)
print('-'*30)
print(df2.head(2))
print('-'*30)
print(df2.tail(2))
print('-'*30)
print(df2.index)
print(df2.columns)
print(datesDF.describe())
print(df2.T)
print(df2['Name'])
print(df2.loc[:, ['Name', 'Job']])
print(df2.iloc[3])
s1 = pd.Series(np.random.randint(0, 7, size=10))
print(s1)
s2 = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s2.str.lower())