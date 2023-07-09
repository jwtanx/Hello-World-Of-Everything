# PySpark Quick Refresh

---

## Basic imports
```py
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.window import Window

# Setting the spark session
app_name = 'Insert-Project-Name'
spark = DataFunctions.getSparkSession(app_name)
```


## Getting the type of the dataframe
print(df.)



## Casting / Changing the type of the data
[Reference](https://sparkbyexamples.com/pyspark/pyspark-cast-column-type/)
```py
df.withColumn("age", df.age.cast(IntegerType()))
```

## Dropping row with null values
[Reference](https://sparkbyexamples.com/pyspark/pyspark-drop-rows-with-null-values/)



## Finding the list of the columns which has the different values
Reference
```py
from pyspark.sql.functions import col, array, when, array_remove

df1 = spark.createDataFrame([
  [1, "ABC", 5000, "US"],
  [2, "DEF", 4000, "UK"],
  [3, "GHI", 3000, "JPN"],
  [4, "JKL", 4500, "CHN"]
], ["id", "name", "sal", "Address"])

df2 = spark.createDataFrame([
  [1, "ABC", 5000, "US"],
  [2, "DEF", 4000, "CAN"],
  [3, "GHI", 3500, "JPN"],
  [4, "JKL_M", 4800, "CHN"]
], ["id", "name", "sal", "Address"])


def select_expr(left_df, right_df, on_col):
  conditions_ = [when(left_df[c]!=right_df[c], lit(c)).otherwise("") for c in right_df.columns if c != 'id']

  select_expression = [col(on_col), 
                      *[left_df[c] for c in left_df.columns if c != 'id'], 
                      array_remove(array(*conditions_), "").alias("column_names")
                      ]

  return select_expression

df1.join(df2, "id").select(select_expr(df1, df2, "id")).show()
```
```
# https://stackoverflow.com/questions/60279160/compare-two-dataframes-pyspark
def get_df_diff(left_df, right_df, on_col, output_col):

  conditions_ = [when(left_df[c]!=right_df[c], lit(c)).otherwise("") for c in left_df.columns if c != on_col]

  select_expression = [col(on_col), 
                        *[left_df[c] for c in left_df.columns if c != on_col], 
                        array_remove(array(*conditions_), "").alias(output_col)
                      ]
  
  return left_df.join(right_df, on_col).select(select_expression)
```



https://sparkbyexamples.com/pyspark/pyspark-where-filter/
https://stackoverflow.com/questions/42983444/filtering-rows-with-empty-arrays-in-pyspark
https://www.projectpro.io/article/pyspark-joins-for-data-analysis-by-example/564#mcetoc_1fsdoe8mdd
https://sparkbyexamples.com/pyspark/convert-pyspark-dataframe-column-to-python-list/
https://sparkbyexamples.com/pyspark/pyspark-convert-array-column-to-string-column/

https://sparkbyexamples.com/pyspark/pyspark-orderby-and-sort-explained/


## Getting the first index value of the specified columns
df.first()['column name']

## Creating PySpark Dataframe
https://sparkbyexamples.com/pyspark/different-ways-to-create-dataframe-in-pyspark/

```py
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
data2 = [("James","","Smith","36636","M",3000),
    ("Michael","Rose","","40288","M",4000),
    ("Robert","","Williams","42114","M",4000),
    ("Maria","Anne","Jones","39192","F",4000),
    ("Jen","Mary","Brown","","F",-1)
  ]

schema = StructType([ \
    StructField("firstname",StringType(),True), \
    StructField("middlename",StringType(),True), \
    StructField("lastname",StringType(),True), \
    StructField("id", StringType(), True), \
    StructField("gender", StringType(), True), \
    StructField("salary", IntegerType(), True) \
  ])
 
df = spark.createDataFrame(data=data2,schema=schema)
df.printSchema()
df.show(truncate=False)
```


## Converting PySpark Dataframe to Dict
https://stackoverflow.com/questions/41206255/convert-pyspark-sql-dataframe-dataframe-type-dataframe-to-dictionary
```py
list_persons = map(lambda row: row.asDict(), df.collect())
```

## Converting Nested PySpark Dataframe into Dict
https://spark.apache.org/docs/3.1.2/api/python/reference/api/pyspark.sql.Row.asDict.html
```py
row = df.collect()[0]
row.asDict(True)
```

## Creating nested pyspark dataframe with struct
```py
structureData = [
    (("James","","Smith"),"36636","M",3100),
    (("Michael","Rose",""),"40288","M",4300),
    (("Robert","","Williams"),"42114","M",1400),
    (("Maria","Anne","Jones"),"39192","F",5500),
    (("Jen","Mary","Brown"),"","F",-1)
  ]
structureSchema = StructType([
        StructField('name', StructType([
             StructField('firstname', StringType(), True),
             StructField('middlename', StringType(), True),
             StructField('lastname', StringType(), True)
             ])),
         StructField('id', StringType(), True),
         StructField('gender', StringType(), True),
         StructField('salary', IntegerType(), True)
         ])

df2 = spark.createDataFrame(data=structureData,schema=structureSchema)
df2.printSchema()
df2.show(truncate=False)
```

## PySpark Data type
https://sparkbyexamples.com/pyspark/pyspark-sql-types-datatype-with-examples/

## Creating new columns or apply new data to the columns
https://sparkbyexamples.com/pyspark/pyspark-withcolumn/

## Convert the datetime to timestamp
https://sparkbyexamples.com/pyspark/pyspark-withcolumn/

```py
df.withColumn('local_ts', date_format(df.date_time, "yyyy-MM-dd HH:mm:ss.SSSX")) \
  .withColumn("timestamp_utc",to_utc_timestamp(to_timestamp(df.date_time, "yyyy-MM-dd HH:mm:ss.SSSX"), 'America/New_York')) \
  .show(10, False) 

# America/New_York is machine's timezone
```
|Col1|date_time                    |local_ts                  |timestamp_utc          |
|----|-----------------------------|--------------------------|-----------------------|
|a   |2020-09-08 14:00:00.917+02:00|2020-09-08 08:00:00.917-04|2020-09-08 12:00:00.917|
|b   |2020-09-08 14:00:00.900+01:00|2020-09-08 09:00:00.900-04|2020-09-08 13:00:00.9  |


## Update a columnd with updated value
https://sparkbyexamples.com/pyspark/pyspark-update-a-column-with-value/
```py
df3 = df.withColumn("gender", when(df.gender == "M","Male") \
      .when(df.gender == "F","Female") \
      .otherwise(df.gender))

# https://stackoverflow.com/questions/48389438/compare-two-columns-to-create-a-new-column-in-spark-dataframe
df.withColumn('flag', F.when((F.col("a") <= 2) | (F.col("b") <= 2), 1).otherwise(2)).show()

```

## Checking if the column data is null
```py
df.withColumn("concat_custom", concat(
  when(df.a.isNull(), lit('_')).otherwise(df.a), 
  when(df.b.isNull(), lit('_')).otherwise(df.b))
)
```

## Trimming the whitespace
https://stackoverflow.com/questions/35155821/trim-string-column-in-pyspark-dataframe
```py
from pyspark.sql.functions import trim
df = df.withColumn("Product", trim(df.Product))

```


## Deep copy dataframe
```py
df2 = df.alias('df2')
```

https://stackoverflow.com/questions/58310246/how-to-concatenate-to-a-null-column-in-pyspark-dataframe
https://stackoverflow.com/questions/44667565/pyspark-dataframe-changing-two-columns-at-the-same-time-based-on-condition

## Getting the distinct value in a list
```py
dfTaskResults.select("state").distinct().toPandas()["state"].tolist()
```