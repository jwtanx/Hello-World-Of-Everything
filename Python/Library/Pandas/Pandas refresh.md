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

## Randomly generate a dataframe
[Reference](https://stackoverflow.com/questions/32752292/how-to-create-a-dataframe-of-random-integers-with-pandas)
```py
# Method 1
df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))

# Method 2: Recommended way
rng = np.random.default_rng()
df = pd.DataFrame(rng.integers(0, 100, size=(100, 4)), columns=list('ABCD'))

```

## Simplest way to create a dataframe for testing
```py
df = pd.DataFrame('x', index=range(3), columns=list('abcd'))
df
'''
   a  b  c  d
0  x  x  x  x
1  x  x  x  x
2  x  x  x  x
'''

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
df3 = pd.DataFrame([[1, 2], [7, 8]], columns=list('AB'), index=['x', 'y'])
df = df1.append(df2)
df
'''
   A  B
x  1  2
y  3  4
x  5  6
y  7  8
'''

df = df1.append([df2, df3])
df
'''
   A  B
x  1  2
y  3  4
x  5  6
y  7  8
x  1  2
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
df = pd.concat([pd.DataFrame([i], columns=['A']) for i in range(5)], ignore_index=True)
df = pd.concat([df1, df2, df3])

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

## INSERTING A NEW COLUMN WITH ALL EMPTY LIST FOR EACH OF THE CELLS
[Reference](https://stackoverflow.com/questions/31466769/add-column-of-empty-lists-to-dataframe)
```py
import numpy as np

# Faster method
df['empty_list'] = np.empty((len(df), 0)).tolist()

# Extra note
np.empty((5, 0)).tolist() # [[], [], [], [], []]

# Slower method
df['empty_list'] = [[] for _ in range(len(df))]

```

## CHECK IF A DATAFRAME IS EMPTY
[Reference](https://stackoverflow.com/questions/19828822/how-to-check-whether-a-pandas-dataframe-is-empty)
```py
if df.empty:
    print("df is empty")
```

## Re-ordering the columns order
```py
# Let's say the df is as below
"""
          0         1         2         3         4      mean
0  0.445598  0.173835  0.343415  0.682252  0.582616  0.445543
1  0.881592  0.696942  0.702232  0.696724  0.373551  0.670208
2  0.662527  0.955193  0.131016  0.609548  0.804694  0.632596
3  0.260919  0.783467  0.593433  0.033426  0.512019  0.436653
4  0.131842  0.799367  0.182828  0.683330  0.019485  0.363371
5  0.498784  0.873495  0.383811  0.699289  0.480447  0.587165
6  0.388771  0.395757  0.745237  0.628406  0.784473  0.588529
7  0.147986  0.459451  0.310961  0.706435  0.100914  0.345149
8  0.394947  0.863494  0.585030  0.565944  0.356561  0.553195
9  0.689260  0.865243  0.136481  0.386582  0.730399  0.561593
"""

# We want to put the "mean" column to the first column
df = df[['mean', '0', '1', '2', '3']]
"""
       mean         0         1         2         3         4
0  0.445543  0.445598  0.173835  0.343415  0.682252  0.582616
1  0.670208  0.881592  0.696942  0.702232  0.696724  0.373551
2  0.632596  0.662527  0.955193  0.131016  0.609548  0.804694
3  0.436653  0.260919  0.783467  0.593433  0.033426  0.512019
4  0.363371  0.131842  0.799367  0.182828  0.683330  0.019485
5  0.587165  0.498784  0.873495  0.383811  0.699289  0.480447
6  0.588529  0.388771  0.395757  0.745237  0.628406  0.784473
7  0.345149  0.147986  0.459451  0.310961  0.706435  0.100914
8  0.553195  0.394947  0.863494  0.585030  0.565944  0.356561
9  0.561593  0.689260  0.865243  0.136481  0.386582  0.730399
"""

```

## Exporting dataframe to csv
[Reference](https://datatofish.com/export-dataframe-to-csv/)
```py
# Index is set to False so there is no index when reading the csv using pandas later
df.to_csv(r'Path where you want to store the exported CSV file\File Name.csv', index=False)

```

## Loading the csv into the dataframe
[Reference](https://stackoverflow.com/questions/20107570/removing-index-column-in-pandas-when-reading-a-csv)
```py
df = pd.read_csv('file_name.csv')
print(df)

# To read the csv without the index
df = pd.read_csv('file_name.csv', index_col=False)

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
df = pd.DataFrame({'A': [0, 1, 0, 3, 4], 'B': [5, 6, 0, 8, 0], 'C': ['a', 'b', 'c', 'd', 'e']})
df.replace(0, 5)
df
'''
   A  B  C
0  5  5  a
1  1  6  b
2  5  5  c
3  3  8  d
4  4  5  e
'''
```

## Replace the value throughout the whole df according to the datatype of the columns (NOT APPLICABLE FOR None)
Why not applicable? Because the code below the column will not be included into the list when there is any one of the data in the column is None
[Reference](https://stackoverflow.com/questions/23743460/replace-none-with-nan-in-pandas-dataframe)
```py
import numpy as np

# Getting only the list of columns that you want to be replaced
obj_columns = list(df.select_dtypes(include=['int']).columns.values)
df[obj_columns] = df[obj_columns].replace(['old'], 'new')

# Example
df = pd.DataFrame({'A': [3, 1, 3, 3, 4], 'B': [5, 6, 3, 8, 0], 'C': ['a', 'b', 'c', 'd', 'e']})
#    A  B  C
# 0  3  5  a
# 1  1  6  b
# 2  3  3  c
# 3  3  8  d
# 4  4  0  e

obj_columns = list(df.select_dtypes(include=['int']).columns.values)
df[obj_columns] = df[obj_columns].replace([3], np.nan)
#      A    B  C
# 0  NaN  5.0  a
# 1  1.0  6.0  b
# 2  NaN  NaN  c
# 3  NaN  8.0  d
# 4  4.0  0.0  e

```

## SIMPLE REPLACING THE NONE VALUE
But take note of the problem as mentioned: If you use df.replace([None], np.nan, inplace=True), this changed all datetime objects with missing data to object dtypes. So now you may have broken queries unless you change them back to datetime which can be taxing depending on the size of your data.
```py
import numpy as np
df = df.replace([None], np.nan)

# Take note: This produces an error
df = df.replace(None, np.nan) # ERROR
# TypeError: 'regex' must be a string or a compiled regular expression or a list or dict of strings or regular expressions, you passed a 'bool'

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

# Removing the first column
df.drop(df.columns[0], inplace=True, axis=1)

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
df = df.drop(['C', 'D'], axis = 1)
df = df.drop(columns=['C', 'D'])
df = df.drop(df.columns[[0, 1, 3]], axis=1) # index starting from 0
  
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

## Removing some row randomly
[Reference](https://stackoverflow.com/a/54955082)
```py
to_remove = np.random.choice(df[df["Discount"]==True].index, size=1068, replace=False) # size = number of rows to be removed
df = df.drop(to_remove)
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

concatenated_dataframes = pd.concat([dataframe1, dataframe2], axis=1) # axis=1 is column, meaning concat horizontally
# If axis=0, we are concatenating the dfs vertically but makes sure the columns are the same
concatenated_dataframes
'''
   0  1  0  1
0  1  2  2  1
1  4  5  5  4
'''
```

## Concatenate the dataframe vertically
[Reference](https://www.geeksforgeeks.org/how-to-combine-two-dataframe-in-python-pandas/)
```py
import pandas as pd
# First DataFrame
df1 = pd.DataFrame({'id': ['A01', 'A02', 'A03', 'A04'],
                    'Name': ['ABC', 'PQR', 'DEF', 'GHI']})
  
# Second DataFrame
df2 = pd.DataFrame({'id': ['B05', 'B06', 'B07', 'B08'],
                    'Name': ['XYZ', 'TUV', 'MNO', 'JKL']})
  
df3 = pd.DataFrame({'City': ['MUMBAI', 'PUNE', 'MUMBAI', 'DELHI'],
                    'Age': ['12', '13', '14', '12']})
  
  
# appending multiple DataFrame
result = df1.append([df2, df3])
display(result)
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

## Saving dataframe to EXCEL
[Reference]()
```py
df.to_excel("test.xlsx", header=True, index=False)
```

## Problem with EXCEL unable to handle timeframe with timezone
[Reference](https://stackoverflow.com/questions/61802080/excelwriter-valueerror-excel-does-not-support-datetime-with-timezone-when-savin)
```py
# df['date'] = old_dates
df['date'] = df['date'].apply(lambda a: pd.to_datetime(a).date()) # .date() removes timezone
```

## Dropping the last row of the dataframe
[Reference](https://thispointer.com/drop-last-row-of-pandas-dataframe-in-python-3-ways/)
```py
# Method 1: Using iloc
# df = df.iloc[row_start:row_end , col_start:col_end]
df = df.iloc[:-1, :]

# Method 2: Using slice
# df = df[row_start:row_end, col_start:col_end]
df = df[:-1, :]

# Method 3: Using drop
df = df.drop(index=df.index[-1], axis=0)

# Method 4: Using the len, when you do not have unique index
df = df[:len(df)-1]

```

## Getting the first column name
```py
col_1_name = df.columns[0]

```

## Getting the first column series or list
[Reference](https://stackoverflow.com/questions/15360925/how-to-get-the-first-column-of-a-pandas-dataframe-as-a-series)
```py
# Method 1
s = df[df.columns[0]]
# Converting it to list
ls = df[df.columns[0]].tolist()

# Method 2: 'Name' is the column name
ls = df.Name.tolist()

```

## How to set a column as an index
[Reference](https://stackoverflow.com/questions/38542419/could-pandas-use-column-as-index)
```py
# Method 1
df = df.set_index('No.')
df.set_index('No.', inplace=True)

# Method 2
# Example of setting the first column to be the index
df = df.set_index(df.columns[0])

```

## How to unset the index or reset the index
[Reference](https://www.delftstack.com/howto/python-pandas/pandas-remove-index/)
```py
# Method 1: Normal resetting and add back the index as column_0
df = df.reset_index()

# Method 2: Resetting + removing the column of the index
df = df.reset_index(drop=True)

# Method 3 : With the inplace, so you do not need to reassign the df
df.reset_index(drop=True, inplace=True)
```

## Updating / Changing the value of a cell
```py
# df.xxx[row, column]

df.at[1, 'Col_2'] = 10
df.loc[1, 'Col_2'] = 10

df.iat[1, 2] = 10
df.iloc[1, 2] = 10

# Which is faster? Comparison: https://stackoverflow.com/questions/37757844/pandas-df-locz-x-y-how-to-improve-speed
In [37]: %timeit df.loc[random.randint(0, 10**7), 'b']
1000 loops, best of 3: 502 µs per loop

In [38]: %timeit df.iloc[random.randint(0, 10**7), 1]
1000 loops, best of 3: 394 µs per loop

In [39]: %timeit df.at[random.randint(0, 10**7), 'b']
10000 loops, best of 3: 66.8 µs per loop

In [41]: %timeit df.iat[random.randint(0, 10**7), 1]
10000 loops, best of 3: 32.9 µs per loop

# NOTE: `iloc` is slower but it can be used to get the list of data for a particular row while `iat` cannot

```

## UPDATING MULTIPLE CELLS
```py
# This will update the first row cells that are in column 1 and column 2 to 10
df.loc[0, ['Col_1' ,'Col_2']] = 10

```

## GETTING THE DATA FOR THE PARTICULAR ROW
```py
# Use iloc to get the data row
print(df.iloc[1])
# a    ABU
# b    TIM
# c    ALI

print(list(df.iloc[1]))
# ['ABU', 'TIM', 'ALI']

```

## Updating / Changing the values of the whole column
```py
df[df.columns[0]] = list(range(1, len(df)+1))
```

## CHANGING THE VALUE FOR THE WHOLE COLUMN
```py
# Method 1
df = df.assign(industry='yyy')

# Method 2
df = df_all.loc[df_call['industry']==specific_id,:].copy()
df['industry'] = 'yyy'

# Method 3
df.loc[:,'industry'] = 'yyy'

```

## Different conversion of df to JSON
[Reference #1](https://stackoverflow.com/questions/28590663/pandas-dataframe-to-json-without-index)
```py
# Method 1: Getting the list of dictionaries for each row: 
# Best converting to dictionary and returning them as a list
dic = df.to_dict(orient='records') 
# [{'A': 46, 'B': 75, 'C': 94, 'D': 43}, {'A': 32, 'B': 78, 'C': 85, 'D': 61}]

# ============================== #

# Method 2: Getting the list of dictionaries for each row.
df_dict = df.reset_index().to_dict(orient='index') 
df_vals = list(df_dict.values())
# [{'index': 0, 'A': 46, 'B': 75, 'C': 94, 'D': 43}, {'index': 1, 'A': 32, 'B': 78, 'C': 85, 'D': 61}]

dic = df.to_dict('index') # To remove the index in the dictionary
ls = list(dic.values())
# [{'A': 46, 'B': 75, 'C': 94, 'D': 43}, {'A': 32, 'B': 78, 'C': 85, 'D': 61}]

# ============================== #

# Method 3: Getting the list of dictionaries for each row. (Returning a string)
json_obj = df.reset_index().to_json(orient='records')
# '[{"index":0,"A":46,"B":75,"C":94,"D":43},{"index":1,"A":32,"B":78,"C":85,"D":61}]'

json_obj = df.to_json(orient='records') # To remove the index in the dictionary
# '[{"A":46,"B":75,"C":94,"D":43},{"A":32,"B":78,"C":85,"D":61}]'

```
[Reference #2](https://stackoverflow.com/questions/26716616/convert-a-pandas-dataframe-to-a-dictionary/26716774#26716774)
```py
# dict - the default: column names are keys, values are dictionaries of index:data pairs
df.to_dict('dict')
{'a': {0: 'red', 1: 'yellow', 2: 'blue'}, 
 'b': {0: 0.5, 1: 0.25, 2: 0.125}}

# list - keys are column names, values are lists of column data
df.to_dict('list')
{'a': ['red', 'yellow', 'blue'], 
 'b': [0.5, 0.25, 0.125]}

# series - like 'list', but values are Series
df.to_dict('series')
{'a': 0       red
      1    yellow
      2      blue
      Name: a, dtype: object, 

 'b': 0    0.500
      1    0.250
      2    0.125
      Name: b, dtype: float64}

# split - splits columns/data/index as keys with values being column names, data values by row and index labels respectively
df.to_dict('split')
{'columns': ['a', 'b'],
 'data': [['red', 0.5], ['yellow', 0.25], ['blue', 0.125]],
 'index': [0, 1, 2]}

# records - each row becomes a dictionary where key is column name and value is the data in the cell
df.to_dict('records')
[{'a': 'red', 'b': 0.5}, 
 {'a': 'yellow', 'b': 0.25}, 
 {'a': 'blue', 'b': 0.125}]

# index - like 'records', but a dictionary of dictionaries with keys as index labels (rather than a list)
df.to_dict('index')
{0: {'a': 'red', 'b': 0.5},
 1: {'a': 'yellow', 'b': 0.25},
 2: {'a': 'blue', 'b': 0.125}}

```
[Reference #3](https://pandas.pydata.org/pandas-docs/version/0.23.3/generated/pandas.DataFrame.to_json.html)
```py
# Horizontal data
df.to_json(orient='index')
# '{"row 1":{"col 1":"a","col 2":"b"},"row 2":{"col 1":"c","col 2":"d"}}'

# Vertical data
df.to_json(orient='columns')
# '{"col 1":{"row 1":"a","row 2":"c"},"col 2":{"row 1":"b","row 2":"d"}}'

# Only value no key
df.to_json(orient='values')
# '[["a","b"],["c","d"]]'

# Getting the schema
df.to_json(orient='table')
# '{"schema": {"fields": [{"name": "index", "type": "string"},
#                         {"name": "col 1", "type": "string"},
#                         {"name": "col 2", "type": "string"}],
#              "primaryKey": "index",
#              "pandas_version": "0.20.0"},
#   "data": [{"index": "row 1", "col 1": "a", "col 2": "b"},
#            {"index": "row 2", "col 1": "c", "col 2": "d"}]}'

```

## Setting the datetime format for the dataframe before converting to json
[Reference](https://stackoverflow.com/questions/52730953/pandas-to-json-output-date-format-in-specific-form)
```py
# Changing the output from "2018-09-17T00:00:00Z":{" to "2018-09-17":{"
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

```

## Updating / Renaming the column name of the dataframe
[Reference](https://stackoverflow.com/questions/11346283/renaming-column-names-in-pandas)
```py
# Reassigning for all the headers
# Method 1
df.columns = ['x', 'y', 'z']

# Method 2
df2 = df.set_axis(['x', 'y', 'z'], axis=1, inplace=False)

# =================================== #
# Renaming only for a certain columns #

# Method 1
df2 = df.rename({'a': 'X', 'b': 'Y'}, axis=1)  # new method
df2 = df.rename({'a': 'X', 'b': 'Y'}, axis='columns')
df2 = df.rename(columns={'a': 'X', 'b': 'Y'})  # old method

# Method 2: inplace
df.rename({'a': 'X', 'b': 'Y'}, axis=1, inplace=True)
df.rename({df.columns[1]: 'Y'}, axis=1, inplace=True)

```

## Formatting the header name of the dataframe using lambda
```py
df.rename(columns=lambda x: x.replace(' ', '_'), inplace=True)
df.rename(columns=lambda x: x.lstrip(), inplace=True)
df.rename(columns=lambda x: x[1:], inplace=True)
df.columns = df.columns.str.replace(' ', '_')

```

## Checking if there is a None in a df
```py
first_col_list = list(df[df.columns[0]])

if pd.isna(first_col_list[i]):
    print('This is a None')

# NOTE: We cannot check with the syntax `first_col_list[i] == None`
```

## SPLITTING THE DATA IN A CELL TO CREATE NEW MULTIPLE ROWS
[Reference](https://stackoverflow.com/questions/12680754/split-explode-pandas-dataframe-string-entry-to-separate-rows/40449726#40449726)

```py


```

## FILTERING THE DATA OR QUERY THE DF (.query)
[Reference](https://stackoverflow.com/questions/11869910/pandas-filter-rows-of-dataframe-with-operator-chaining?rq=1)
```py
# Method 1: Using normal multiple filterinig at the same time
In [99]: df[(df.A == 1) & (df.D == 6)]
Out[99]:
   A  B  C  D
d  1  3  9  6

# Method 2: Using chaining condition, filtering after one condition before going to check for the next condition
df = pd.DataFrame(np.random.randn(30, 3), columns=['a','b','c'])
df_filtered = df.query('a > 0').query('0 < b < 2')
# Single query
df_filtered = df.query('a > 0 and 0 < b < 2')

```

## QUERY THE DF AND GET THE INDEX FROM IT
[Reference](https://www.skytowner.com/explore/getting_indexes_of_rows_matching_conditions_in_pandas_dataframe)
```py
# Method 1: Getting the indexes in a list
indexes = df.query("a == 1").index.tolist()
# Note: You do not need to change the indexes to list to extract the first index
df.query("a == 1").index[0]

# Method 2: Get the indexes in a numpy array          
df.index.get_indexer(df.query("a == 3").index)
```

## UPDATING THE FIELD IF A CONDITION IS MET (UPDATE TWO COLUMNS AT THE SAME TIME)
[Reference](https://stackoverflow.com/questions/36909977/update-row-values-where-certain-condition-is-met-in-pandas)
```py
# Updating one column only
df1.loc[df1['category'] == 2, 'green_area'] = 'YES'
print(df1)
   category   green_area  yellow_area
a       1     some_value   some_value
b       2            YES   some_value
c       2            YES   some_value
d       3     some_value   some_value

# Updating two columns are the same time
df1.loc[df1['category'] == 2, ['green_area', 'yellow_area']] = 'YES'
print(df1)
   category   green_area  yellow_area
a       1     some_value   some_value
b       2            YES          YES
c       2            YES          YES
d       3     some_value   some_value
```

## UPDATING THE FIELD WITH TWO DIFFERENT VALUE IF XXX THEN A ELSE B (NP.WHERE)
```py
df1['feat'] = np.where(df1['stream']==2, 10, 20)
print(df1)
   stream  feat another_feat
a       1    20   some_value
b       2    10   some_value
c       2    10   some_value
d       3    20   some_value
```

## APPLYING THE CALCULATION TO THE CELLS THAT MATCH THE REQUIREMENT
```py
print(df1)
   stream  feat  another_feat
a       1     4             5
b       2     4             5
c       2     2             9
d       3     1             7

#filter columns all without stream
cols = [col for col in df1.columns if col != 'stream']
print cols
['feat', 'another_feat']

df1.loc[df1['stream'] == 2, cols ] = df1 / 2
print(df1)
   stream  feat  another_feat
a       1   4.0           5.0
b       2   2.0           2.5
c       2   1.0           4.5
d       3   1.0           7.0

```

## NEW COLUMN, DATA ADDED WITH MULTIPLE CONDITION WITH MULTIPLE DIFFERENT VALUES (NP.WHERE, NP.SELECT)
```py
df0 = pd.DataFrame({'Col':[5,0,-6]})

df0['New Col1'] = np.where((df0['Col'] > 0), 'Increasing', 
                          np.where((df0['Col'] < 0), 'Decreasing', 'No Change'))

df0['New Col2'] = np.select([df0['Col'] > 0, df0['Col'] < 0],
                            ['Increasing',  'Decreasing'], 
                            default='No Change')

print (df0)
   Col    New Col1    New Col2
0    5  Increasing  Increasing
1    0   No Change   No Change
2   -6  Decreasing  Decreasing

```


## CHANGING THE VALUES OF A COLUMN BASED ON THE OTHER COLUMN (== or .eq [equal])
[Reference](https://stackoverflow.com/questions/63768410/how-to-modify-original-dataframe-after-updating-its-value-off-of-a-filtered-view)
[Reference](https://stackoverflow.com/questions/49161120/pandas-python-set-value-of-one-column-based-on-value-in-another-column)
```py
         col_0   col_1
0    'Blood B'    'OK'
1    'Blood A'    'NO'
2    'Blood B'    'NO'

df.loc[df['col_0'] == 'Blood B', 'col_1'] = 'CHANGES'

         col_0        col_1
0    'Blood B'    'CHANGES'
1    'Blood A'         'NO'
2    'Blood B'    'CHANGES'

# df.loc[df['SPORT'].eq('Tennis'), 'TEST'] = 'CHANGED'

```

## MATCHING THE VALUE OF THE CELLS OF A COLUMNS WITH A LIST, THEN APPLY NEW VALUE TO THE CORRESSPONDING CELL (.isin [IN])
[Reference](https://stackoverflow.com/questions/44218378/comparison-of-a-dataframe-column-values-with-a-list)
```py
import pandas as pd

df = pd.DataFrame([[[1,2,3,4], 5, "john"], [[5,6,7,8], 0, "alex"], [[5,6,7,8], 2, "stacy"]], columns=["num", "age", "name"])
df
"""
            num  age   name
0  [1, 2, 3, 4]    5   john
1  [5, 6, 7, 8]    9   alex
2  [5, 6, 7, 8]    2  stacy
"""

df.loc[df["add"].isin({1,2,3,4,5}), "name"] = "baby" # Using set rather than list for the [1,2,3,4,5] for faster matching
df
"""
            one  add  name
0  [1, 2, 3, 4]    5  baby
1  [5, 6, 7, 8]    0  alex
2  [5, 6, 7, 8]    2  baby
"""

# Can return the matching as true / false too then you can also convert the type of the returned into integer
df['D'] = df.C.isin(firsts).astype(int)

df
#   A   B   C   D
#0  1   10  100 1
#1  1   15  150 0
#2  2   20  200 1
#3  2   25  250 0
#4  3   30  300 1
#5  3   35  350 0

```

## RETURNING A LIST THAT THE ELEMENT WITHIN IT MATCHES WITH A LIST OF ELEMENTS [USING FILTER]
[Reference](https://stackoverflow.com/questions/72319308/compare-each-element-in-a-list-with-a-column-of-lists-in-a-dataframe-python)
```py
lst = ['apple', 'orange', 'banana']
df['match'] = df['fruits'].apply(lambda ls: list(filter(lambda x: x in lst, ls)))
print(df)
"""
                   fruits            match
0  [apple, orange, berry]  [apple, orange]
1                [orange]         [orange]
"""
```

## STRING SEARCHING IN DATAFRAME
[Reference](https://towardsdatascience.com/check-for-a-substring-in-a-pandas-dataframe-column-4b949f64852?gi=a0358f34659)
```py


```

## FILTERING THE DF BASED ON THE STRING LENGTH
[Reference](https://stackoverflow.com/questions/19937362/filter-string-data-based-on-its-string-length)
```py
# Slow but working
df["text"] = df["text"].apply(lambda x: x if len(x) >= 10 else np.nan)

# Alternative approach
df = df[df["A"].apply(lambda x: len(str(x)) == 10)]
df = df[(df["A"].astype(str).str.len() == 10) & (df["B"].astype(str).str.len() == 10)]

```

## SELECTING THE OPTION FOR THE CELL BASED ON THE OTHER COLUMNS DATA
[Reference](https://stackoverflow.com/questions/54893547/edit-data-in-a-python-pandas-filter-and-apply-it-to-the-original-data-frame)
```py
zone1 = (df['Latitude'] > 0) & (df['Longitude'] > 0)
zone2 = (df['Latitude'] < 0) & (df['Longitude'] > 0)
zone3 = (df['Latitude'] > 0) & (df['Longitude'] < 0)
zone4 = (df['Latitude'] < 0) & (df['Longitude'] < 0)

df['Zone'] = np.select([zone1,zone2,zone3,zone4],['Z1','Z2', 'Z3','Z4'])
```

## GETTING THE INDEX OF A COLUMN USING ITS NAME
[Reference](https://www.geeksforgeeks.org/get-column-index-from-column-name-of-a-given-pandas-dataframe/)
```py
# dictionary
record = {'Math': [10, 20, 30, 40, 70],
          'Science': [40, 50, 60, 90, 50], 
          'English': [70, 80, 66, 75, 88]}
  
# give column name
col_name = "Science"
  
# find the index no
index_no = df.columns.get_loc(col_name)
  
print("Index of {} column in given dataframe is : {}".format(col_name, index_no))
# Index of Science column in given dataframe is : 1
```

## DF TO JSON
```py
# pip install simplejson
# How to export the json null data from df or python that has None value in it?
# df_vals = list(df.T.to_dict().values())
simplejson.loads(simplejson.dumps(list(df.T.to_dict().values()), ignore_nan=True))

# OR...

dic = df.to_dict('index')
df_vals = list(dic.values())
simplejson.loads(simplejson.dumps(df_vals, ignore_nan=True))

```

## GETTING THE UNIQUE VALUES FROM A COLUMN
```py
df['category'].unique().tolist()    
df.category.unique().tolist()
```

## STRIP / REMOVING THE WHITESPACES OF THE CELLS
```py
# https://stackoverflow.com/questions/33788913/pythonic-efficient-way-to-strip-whitespace-from-every-pandas-data-frame-cell-tha
data_frame_trimmed = data_frame.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
```

## REPLACING THE WORD USING REGEX
```py
df = df.replace('_x000D_', '', regex=True)
```

## REVIEWING SOME OF THE ROW THAT HAS MISSING VALUE
[Reference](https://stackoverflow.com/questions/14247586/how-to-select-rows-with-one-or-more-nulls-from-a-pandas-dataframe-without-listin)
```py
print(df[(df.isnull().sum(axis=1) >= 1)].index)
# Int64Index([142666, 142667, 195148, 195149, 270009, 270010, 270011], dtype='int64')

df.loc[df.isnull().any(axis=1)]
```

## DROPPING THE ROWS WITH NaN VALUE
```py
df = df.dropna()
df = df.dropna().reset_index(drop=True)

# Double confirm if the row with NaN are removed
df.loc[df.isnull().any(axis=1)]
```

## DROPPING THE ROWS WITH SOME MATCHING CONDITIONS
[Reference](https://sparkbyexamples.com/pandas/pandas-drop-rows-with-condition/)
```py
df.drop(df[(df["Price"] >= 24000) | (df["Discount"] == 1)].index, inplace=True)

# Matching the rows with no string
# Checking the least amount of length for the string of each row
df.sort_values(by="Name", key=lambda x: x.str.len())
df = df[df["Name"].astype(str).str.len() > 0].reset_index(drop=True)

```

## FATEST WAYS TO GET THE VALUE COUNT
[Reference](https://stackoverflow.com/questions/35277075/python-pandas-counting-the-occurrences-of-a-specific-value)
```py
(df["COL_NAME"].values == "A").sum()
```

## DROPPING THE DUPLICATED ROW OF DATA
```py
df = pd.DataFrame({'A': [0,0,2,3,4], 'B': [0,0,2,3,4], 'C': ['a', 'a', 'c', 'd', 'e']})

df.drop_duplicates(keep=False, inplace=True) # Not keeping any duplicated value even the unique one will be removed too
df.drop_duplicates(keep="first", inplace=True) # Keeping the first duplicated value
df.drop_duplicates(keep="last", inplace=True) # Keeping the last duplicated value

df = df.drop_duplicates(keep="first").reset_index(drop=True)
```
## REMOVE COLUMNS / DROP COLUMNS
```py
df = df.drop(['B', 'C'], axis=1)
df = df.drop(columns=['B', 'C'])
```

## DROPPING THE COLUMNS THAT MIGHT OR NOT BE IN THE DATAFRAME
```py
df = df.drop(columns=["A", "B", "COL_NAME_NOT_EXISTS"], errors="ignore")
```

## REDUCE THE MEMORY USAGE
```py
import gc
gc.enable() # Enable the garbage collector
df = pd.read_csv("test.csv")

# https://www.kaggle.com/code/tokakhaled/insta-market-analysis
def reduce_mem_usage(train_data):
    """ Iterate through all the columns of a dataframe and modify the data type to reduce memory usage. """
    start_mem = train_data.memory_usage().sum() / 1024**2
    print('Memory usage of dataframe is {:.2f} MB'.format(start_mem))

    for col in train_data.columns:
        col_type = train_data[col].dtype

        if col_type != object:
            c_min = train_data[col].min()
            c_max = train_data[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    train_data[col] = train_data[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    train_data[col] = train_data[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    train_data[col] = train_data[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    train_data[col] = train_data[col].astype(np.int64)  
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    train_data[col] = train_data[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    train_data[col] = train_data[col].astype(np.float32)
                else:
                    train_data[col] = train_data[col].astype(np.float64)
        else:
            train_data[col] = train_data[col].astype('category')
        end_mem = train_data.memory_usage().sum() / 1024**2
        print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
        print('Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))

    return train_data

reduce_mem_usage(df)
```

## FLITERING OUT THE ROWS WITH SPECIFIC STRING
[Reference](https://www.geeksforgeeks.org/how-to-drop-rows-that-contain-a-specific-string-in-pandas/)
```py
words_to_removes = ["nasty", "funny", "poop"]

df = df[~df["Comment"].str.contains('|'.join(discard), case=False)] # The ~ means "not", case = False if do not want to check the casing

```

## MERGING TWO ROWS BASED ON A VALUE IN A COLUMN
[Reference](https://stackoverflow.com/questions/70248572/how-to-merge-two-rows-with-the-same-value-in-a-given-column)
```py
d = {"Class": ["5S1", "5S1", "U6F", "L6F", "U6F"], 
    "Number": ["ONE", "TWO", "THREE", "FOUR", "FIVE"], 
    "List": [["val1"], ["val2"], ["val3"], ["val4"], ["val5"]],
    "Category_1": [0, 1, 1, 0, 0],
    "Category_2": [1, 0, 0, 1, 1]}
df = pd.DataFrame(d)

"""
  Class Number    List  Category_1  Category_2
0   5S1    ONE  [val1]           0           1
1   5S1    TWO  [val2]           1           0
2   U6F  THREE  [val3]           1           0
3   L6F   FOUR  [val4]           0           1
4   U6F   FIVE  [val5]           0           1
"""

# IMPORTANT: Make sure you create a new df
# Combining the string with \n
df2 = pd.DataFrame(df.groupby("Class")["Number"].apply(lambda x:'\n'.join(x)))

# Appending the list together
df2["List"] = df.groupby("Class")["List"].sum()

# Finding the max for the number
df2["Category_1"] = df.groupby("Class")["Category_1"].max()

# Finding the first for the number
df2["Category_2"] = df.groupby("Class")["Category_2"].first()

df2
"""
            Number          List  Category_1  Category_2
Class
5S1       ONE\nTWO  [val1, val2]           1           1
L6F           FOUR        [val4]           0           1
U6F    THREE\nFIVE  [val3, val5]           1           0
"""

```

## JOINING TWO DATAFRAME BASED ON AN INTERSECTING COLUMNS
[Reference](https://stackoverflow.com/questions/49787325/full-outer-join-of-two-or-more-data-frames)
[More information on join](https://www.analyticsvidhya.com/blog/2020/02/joins-in-pandas-master-the-different-types-of-joins-in-python/)
```py
item_code = pd.DataFrame([["A01", "apple"], ["B01", "banana"]], columns=["code", "name"])
item_price = pd.DataFrame([["A01", 2.99], ["B01", 1.99]], columns=["fruit_code", "price"])
print(item_code)
"""
  code    name
0  A01   apple
1  B01  banana
"""

print(item_price)
"""
  fruit_code  price
0        A01   2.99
1        B01   1.99
"""

# Joining the dataframes
catalogue = item_code.join(item_price.set_index("fruit_code"), on="code", how="left") # left, right, outer, inner
print(catalogue)
"""
  code    name  price
0  A01   apple   2.99
1  B01  banana   1.99
"""
```

## JOINING TWO STRING FROM TWO COLUMNS TOGETHER (ADDING, CONCATENATE STRING)
```py
df = pd.DataFrame([["John", "Cena"], ["Spongebob", "Squarepant"]], columns=["First", "Last"])
"""
       First        Last
0       John        Cena
1  Spongebob  Squarepant
"""

df["Full name"] = df["First"] + " " + df["Last"]
"""
       First        Last             Full name
0       John        Cena             John Cena
1  Spongebob  Squarepant  Spongebob Squarepant
"""

# Drop the other two columns
df = df.drop(columns=["First", "Last"])
```

## APPENDING INTEGER FROM A COLUMN TO ANOTHER COLUMN WITH LIST
[Reference](https://stackoverflow.com/questions/69296253/append-another-column-values-to-pandas-column-with-list-values)
```py
import pandas as pd

df = pd.DataFrame([[[1,2,3,4], 5, "john"], [[5,6,7,8], 0, "alex"]], columns=["one", "add", "name"])
"""
             one  add   name
0   [1, 2, 3, 4]    5   john
1   [5, 6, 7, 8]    0   alex
"""

import numpy as np
df["one"] = df.apply(lambda x : np.append(x['add'], x['one']), axis=1)

"""
                one add name
0   [5, 1, 2, 3, 4] 5   john
1   [0, 5, 6, 7, 8] 0   alex
"""
df.apply(lambda x:  np.append(x['a'], (x['b'], x['c'])), axis=1) # For concatenating three column together
```

## CHANGING THE TYPE OF THE VALUE
[Reference](https://stackoverflow.com/questions/15891038/change-column-type-in-pandas)
```py
df["kg"] = df["kg"].astype(int)
print(df["kg"].dtype) # int64

# Downcasting the int64 to int8
df["kg"] = pd.to_numeric(df[col], downcast='integer')
import numpy as np
df["kg"] = df["kg"].astype(int).astype(np.int8) # Both works
print(df["kg"].dtype) # int8

# Easiest method
df["kg"] = df["kg"].astype("int8")

# Checking all the dtypes of the pandas columm
print(df.dtypes)
```

## SORTING THE DATAFRAME ROW BASED ON THE STRING LENGTH
[Reference](https://stackoverflow.com/questions/42516616/sort-dataframe-by-string-length)
```py
df.sort_values(by="name", key=lambda x: x.str.len())
```

Mask: https://stackoverflow.com/questions/19937362/filter-string-data-based-on-its-string-length
merge: https://www.datasciencemadesimple.com/join-merge-data-frames-pandas-python/