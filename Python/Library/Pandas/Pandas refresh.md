# Pandas Quick Refresh
---
[Official CheatSheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

As always: `import pandas as pd`

## Creating a pandas dataframe
```py
df = pd.DataFrame(columns=['Quadrant', 'Phrase', 'Vertices'])
df = df.append(dict(Quadrant=quadrant, Phrase=description, Vertices=bounds), ignore_index=True)
# Where the variable can be string

```

## Converting numpy to dataframe
[Reference](https://datatofish.com/numpy-array-to-pandas-dataframe/)
```py
import numpy as np
import pandas as pd

my_array = np.array([[11,22,33],[44,55,66]])

df = pd.DataFrame(my_array, columns = ['Column_A','Column_B','Column_C'])

print(df)
'''
Column_A  Column_B  Column_C
0        11        22        33
1        44        55        66
'''

my_array = np.array([['Jon',25,1995,2016],['Maria',47,1973,2000],['Bill',38,1982,2005]], dtype=object)

df = pd.DataFrame(my_array, columns = ['Name','Age','Birth Year','Graduation Year'])

print(df)
'''
    Name Age Birth Year Graduation Year
0    Jon  25       1995            2016
1  Maria  47       1973            2000
2   Bill  38       1982            2005
'''

# Getting the vector from gensim doc2vec model
df = pd.DataFrame(columns=[x for x in range(vec_size)])
for i in range(data_size):
    df = df.append(pd.DataFrame(np.array([model.dv[i]]), columns = [x for x in range(vec_size)]), ignore_index=True)

```

## Appending the data into the dataframe
[Reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.append.html)

```py
# Traditional way
df1 = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'), index=['x', 'y'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'), index=['x', 'y'])
df3 = df1.append(df2)
df3
'''
   A  B
x  1  2
y  3  4
x  5  6
y  7  8
'''

df = pd.DataFrame(columns=['A'])

for i in range(5):
    df = df.append({'A': i}, ignore_index=True)

'''
   A
0  0
1  1
2  2
3  3
4  4
'''

# Another way
pd.concat([pd.DataFrame([i], columns=['A']) for i in range(5)], ignore_index=True)

```

## Adding a new column into the dataframe
[Reference](https://www.geeksforgeeks.org/adding-new-column-to-existing-dataframe-in-pandas/)
```py
# Declare a list that is to be converted into a column
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
  
# Using 'Address' as the column name
# and equating it to the list
df['Address'] = address

```

## Inserting a new column at the before the first column
[Reference](https://stackoverflow.com/questions/18674064/how-do-i-insert-a-column-at-a-specific-column-index-in-pandas)
```py
df = pd.DataFrame({'B': [1, 2, 3], 'C': [4, 5, 6]})

df
Out: 
   B  C
0  1  4
1  2  5
2  3  6

idx = 0
new_col = [7, 8, 9]  # can be a list, a Series, an array or a scalar   
df.insert(loc=idx, column='A', value=new_col)

df
Out: 
   A  B  C
0  7  1  4
1  8  2  5
2  9  3  6

```

## Exporting dataframe to csv
[Reference](https://datatofish.com/export-dataframe-to-csv/)
```py
df.to_csv(r'Path where you want to store the exported CSV file\File Name.csv', index = False)

```

## Loading the csv into the dataframe
```py
df = pd.read_csv ('file_name.csv')
print(df)

```

## Selecting multiple columns
[Reference](https://www.geeksforgeeks.org/how-to-select-multiple-columns-in-a-pandas-dataframe/)
```py
# select two columns
df[['Name', 'Qualification']]

# select all rows and second to fourth column
df[df.columns[1:4]]

# select three rows and two columns
df.loc[1:3, ['Name', 'Qualification']]

# select two rows and column "name" to "Address" Means total three columns
df.loc[0:1, 'Name':'Address']

# Remember that Python does not slice inclusive of the ending index.
# select all rows select first two column
df.iloc[:, 0:2] 

# select all rows and 0 to 2 columns 
print(df.ix[:, 0:2])
```

## Replace the value throughout the whole df
```py
df = pd.DataFrame({'A': [0, 1, 2, 3, 4], 'B': [5, 6, 7, 8, 9], 'C': ['a', 'b', 'c', 'd', 'e']})
df.replace(0, 5)
df
'''
    A  B  C
0  5  5  a
1  1  6  b
2  2  7  c
3  3  8  d
4  4  9  e
'''
```


## Replace the value in a specified column
```py
df = pd.DataFrame({"column1": ["a", "b", "a"]})
print(df)
'''
  column1
0       a
1       b
2       a
'''

df["column1"].replace({"a": "x", "b": "y"}, inplace=True)
print(df)
'''
  column1
0       x
1       y
2       x
'''

```

## Removing a column
```py
# Remove column name 'A'
df = df.drop(['A'], axis=1)

# Remove all columns between column index 1 to 3
df.drop(df.iloc[:, 1:3], inplace = True, axis = 1)

# Remove all columns between column name 'B' to 'D'
df = df.drop(df.ix[:, 'B':'D'].columns, axis = 1)

# Remove all columns between column name 'B' to 'D'
df = df.drop(df.loc[:, 'B':'D'].columns, axis = 1)

# Removing a column with the specified column name
df = df.drop('Category', axis='columns')

```

## Removing multiple column
[Reference](https://www.geeksforgeeks.org/how-to-drop-one-or-multiple-columns-in-pandas-dataframe/)
```py
data = {
    'A':['A1', 'A2', 'A3', 'A4', 'A5'], 
    'B':['B1', 'B2', 'B3', 'B4', 'B5'], 
    'C':['C1', 'C2', 'C3', 'C4', 'C5'], 
    'D':['D1', 'D2', 'D3', 'D4', 'D5'], 
    'E':['E1', 'E2', 'E3', 'E4', 'E5'] }

# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
  
# Remove two columns name is 'C' and 'D'
df.drop(['C', 'D'], axis = 1)
  
# df.drop(columns =['C', 'D'])
'''
    A   B   E
0  A1  B1  E1
1  A2  B2  E2
2  A3  B3  E3
3  A4  B4  E4
4  A5  B5  E5
'''
```

## Understanding the parameter inplace
[Reference](https://stackoverflow.com/questions/43893457/understanding-inplace-true)

Default value is False, which mean it performs the operation and returns a copy of the object, so you'd use:
In order to do the changes you need to assign it to a variable
`df = df.an_operation(inplace=False)` Note that the inplace=False here is not needed as it is the default value

When inplace=True, you do not need to assign the df to a new variable to get the updated value
df.an_operation(inplace=True)

```py
data = {
    'A':['A1', 'A2', 'A3', 'A4', 'A5'], 
    'B':['B1', 'B2', 'B3', 'B4', 'B5'], 
    'C':['C1', 'C2', 'C3', 'C4', 'C5'], 
    'D':['D1', 'D2', 'D3', 'D4', 'D5'], 
    'E':['E1', 'E2', 'E3', 'E4', 'E5'] }

# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
  
# Remove two columns name is 'C' and 'D'
df.drop(['C', 'D'], axis=1)
df
'''
    A   B   C   D   E
0  A1  B1  C1  D1  E1
1  A2  B2  C2  D2  E2
2  A3  B3  C3  D3  E3
3  A4  B4  C4  D4  E4
4  A5  B5  C5  D5  E5
'''

df.drop(['C', 'D'], axis=1, inplace=True)
df
'''
    A   B   E
0  A1  B1  E1
1  A2  B2  E2
2  A3  B3  E3
3  A4  B4  E4
4  A5  B5  E5
'''

```
TL;DR
inplace=True is very dangerous, it is best to use the method below
```py
df = df.drop(['C', 'D'], axis=1)

```

## Concatenate the dataframe horizontally
[Reference](https://www.kite.com/python/answers/how-to-concatenate-pandas-dataframes-horizontally-in-python)
```py
dataframe1 = pd.DataFrame([[1, 2], [4, 5]])
dataframe2 = pd.DataFrame([[2, 1], [5, 4]])

concatenated_dataframes = pd.concat([dataframe1, dataframe2], axis=1) # axis=1 is column
concatenated_dataframes
'''
   0  1  0  1
0  1  2  2  1
1  4  5  5  4
'''
```

## Stripping the column name, removing the left white spaces in the name of the column
```py
train.columns = train.columns.str.lstrip()

```

## Split the data evenly for training and testing when the number of the data is unbalanced
[Reference](https://www.youtube.com/watch?v=Tui5ajW3JF8)
```py
from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_set = train_test_split(X, y, train_size=0.8, random_state=42)
# OR
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=df['Label'])

# Getting the same amount of types for the training and the testing
y1 = y_test.value_counts()
y2 = y_train.value_counts()
tol = y.value_counts()

# y1 / tol ~= y2 / tol according to their classes

```

## Saving dataframe to CSV
[Reference](https://towardsdatascience.com/how-to-export-pandas-dataframe-to-csv-2038e43d9c03?gi=9c65376fa79d)
```py
# Set index=False so that the index will not be showing in the first column
df.to_csv('file_name.csv', index=False)

```