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
df.loc[1, ['Col_1' ,'Col_2']] = 10

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

## FILTERING THE DATA
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

## CHANGING THE VALUES OF A COLUMN BASED ON THE OTHER COLUMN
[Reference](https://stackoverflow.com/questions/63768410/how-to-modify-original-dataframe-after-updating-its-value-off-of-a-filtered-view)
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

## STRING SEARCHING IN DATAFRAME
[Reference](https://towardsdatascience.com/check-for-a-substring-in-a-pandas-dataframe-column-4b949f64852?gi=a0358f34659)
```py



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

## DROPPING THE NaN VALUE
```py
df = df.dropna()

# Double confirm if the row with NaN are removed
df.loc[df.isnull().any(axis=1)]
```

## FATEST WAYS TO GET THE VALUE COUNT
[Reference](https://stackoverflow.com/questions/35277075/python-pandas-counting-the-occurrences-of-a-specific-value)
```py
(df["COL_NAME"].values == "A").sum()
```

## DROPPING THE DUPLICATED ROW OF DATA
```py
df.drop_duplicates(keep=False, inplace=True) # Not keeping any duplicated value even the unique one will be removed too
df.drop_duplicates(keep="first", inplace=True) # Keeping the first duplicated value
df.drop_duplicates(keep="last", inplace=True) # Keeping the last duplicated value
```
## REMOVE COLUMNS
```py
df = df.drop(['B', 'C'], axis=1)
df = df.drop(columns=['B', 'C'])
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