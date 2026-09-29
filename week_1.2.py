import pandas as pd

data = {
    'apple': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}

df = pd.DataFrame(data)
print(df)

data = {
    'col_1': [1, 2, 3, 4],
    'col_2': ['A', 'B', 'C', 'D']
}

df1 = pd.DataFrame.from_dict(data)
print(df1)

data = {
    'row_1': [1, 2, 3, 4],
    'row_2': ['A', 'B', 'C', 'D']
}

df2 = pd.DataFrame.from_dict(data, orient='index')
print(df2)

df3=pd.read_csv('Iris.csv')
print(df3)

df4=pd.read_csv('Iris.csv',index_col=0)
print(df4)

df5 = pd.read_json('sample1.json', typ='series')
print(df5)

data = {
    'Std_Num': [101, 102, 103, 104, 105],
    'Std_Name': ['Revanth', 'Rahul', 'Priya', 'Anu', 'Charan'],
    'Age': [18, 19, 18, 20, 19],
    'Section': ['A', 'B', 'A', 'C', 'B'],
    'Branch': ['CSE', 'ECE', 'CSE', 'IT', 'CSE']
}

df6 = pd.DataFrame(data)
print(df6)
df6.to_csv('student.csv')

df7=pd.read_csv('Iris.csv')
df7.head()
df7.head(10)
df7.tail()
df7.tail(10)
df7.info()
df7.shape
df7.describe()

d={'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df8=pd.DataFrame(d)

print("Adding a new column by passing as Series:")
df8['three'] = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(df8)

print("Adding a new column using the existing columns in DataFrame:")
df8['four'] = df8['one'] + df8['three']
print(df8)

