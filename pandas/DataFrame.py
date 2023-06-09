import pandas as pd
df = pd.DataFrame([1, 2, 3, 4, 5, 6])
print(pd.__version__)
print(df)
print(df)

# reading csv files
df1 = pd.read_csv('C:\\Users\\CSC\\OneDrive\\Documents\\pandas\\Fortune_10.csv', usecols=[0,1,2])
print(df1)

#filtering  rows
df2 = pd.read_csv('C:\\Users\\CSC\\OneDrive\\Documents\\pandas\\Fortune_10.csv', nrows=5)
print(df2)

df3 = pd.read_csv('C:\\Users\\CSC\\OneDrive\\Documents\\pandas\\Fortune_10.csv', usecols=[0,1,2])
print(df3)

#skipping rows(1,2,3) and chanhing the index columns(we can keep any columns as index columns)
df4 = pd.read_csv('C:\\Users\\CSC\\OneDrive\\Documents\\pandas\\Fortune_10.csv', skiprows=[1,2,3],index_col='Name')
print(df4)

# changing(None ,0,1,2) or  the header and header names(a,b,..)

df5 = pd.read_csv('C:\\Users\\CSC\\OneDrive\\Documents\\pandas\\Fortune_10.csv', header = None, names = ['a','b','c','d','e','f','g'])
print(df5)
# exporting the csv from df
df5.to_csv("C:\\Users\\CSC\\PycharmProjects\\pythonProject\\outout\\sample.csv",index = False)

df6 = pd.read_csv('C:\\Users\\CSC\\OneDrive\\Documents\\pandas\\Fortune_10.csv')
print(df6)
print(df6.dtypes)
print(df6.columns)
print(df6.index)
print(df6.describe())
print("info is combination of dtypes + columns +index and also talks about storage")
print(df6.info())
print(df6['Profit'].sum())
print(df6['Profit'].mean())
print("by default head shows 5 records")
print(df6.head)
print(df6.head,10)
print(df6.tail)
print(df6.tail(10))
print(df6.loc[3])
print(df6.iloc[3])
print(df6.iloc[:3])
print(df6.loc[:3])
print(pd.crosstab(df6['Industry'],df6['Profit']))

