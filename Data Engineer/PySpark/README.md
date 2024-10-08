# PySpark Quick Refresh

---

## Basic imports
```py
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.window import Window

# Setting the spark session
app_name = "Insert-Project-Name"
spark = SparkSession.builder.appName(app_name).getOrCreate()

# Creating your first pyspark's dataframe
df = spark.createDataFrame([
      [1, "ABC", 5000, "US"],
      [2, "DEF", 4000, "UK"],
      [3, "GHI", 3000, "JPN"],
      [4, "JKL", 4500, "CHN"]
    ], ["id", "name", "sal", "address"])
```

## Getting the type of the dataframe
```py
print(df.dtypes)
```

## Showing the pyspark dataframe
```py
df.show()

# Vertical parquet format
df.show(vertical=True)

# Avoid truncating the data
df.show(truncate=False)

# Showing only few data
df.show(5)

```

## Limitting the row
```py
df = df.limit(10)

# Limit then only show, faster than df.show(1)
df.limit(1).show()
```

## Casting / Changing the type of the data
https://sparkbyexamples.com/pyspark/pyspark-cast-column-type/
```py
df.withColumn("age", df.age.cast(IntegerType()))
```

## Dropping row with null values
https://sparkbyexamples.com/pyspark/pyspark-drop-rows-with-null-values/


## Drop one or multiple columns
https://sparkbyexamples.com/pyspark/pyspark-drop-column-from-dataframe/
```py
# One column
df = df.drop("firstname")
df = df.drop(col("firstname"))
df = df.drop(df.firstname)

# Multiple columns
cols = ("firstname", "middlename", "lastname")
df = df.drop(*cols)
```

## Selecting only certain columns
https://sparkbyexamples.com/pyspark/select-columns-from-pyspark-dataframe/
```py

# By name
df.select("firstname", "lastname").show()

# By columns index
df.select(df.columns[2:7]).show()

# By using col() function
from pyspark.sql.functions import col
df.select(col("firstname"), col("lastname")).show()

# By nested column
df2.select("name.firstname", "name.lastname").show(truncate=False)

```
## Selecting all columns
```py
df.select("*").show()

# Also can check deep copy
df2 = df.alias("df2")
```

## WHEN, OTHERWIRSE Clause - Finding the list of the columns which has the different values
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

```py
# https://stackoverflow.com/questions/60279160/compare-two-dataframes-pyspark
def get_df_diff(left_df, right_df, on_col, output_col):

  conditions_ = [when(left_df[c]!=right_df[c], lit(c)).otherwise("") for c in left_df.columns if c != on_col]

  select_expression = [col(on_col),
                        *[left_df[c] for c in left_df.columns if c != on_col],
                        array_remove(array(*conditions_), "").alias(output_col)
                      ]

  return left_df.join(right_df, on_col).select(select_expression)
```

## WHERE Clause
https://linuxhint.com/pyspark-where-clause/
```py
# Using property
df = df.where(df.age == 23)
df = df.where(df["age"] == 23)

# Using col function
from pyspark.sql.functions import col
df = df.where(col("age") == 23)

# Using operational to include multiple conditions
df = df.where( (df.age >= 10) & (df.age <= 21) )
df = df.where( (df.age >= 10) | (df.age <= 21) )

# Getting the list of the rows from the filtered dataframe
rows = df.where(df.age == 23).collect()

# Getting the list of the names without the PySpark's Row object using flatMap
value_rows = df.where(df.age == 23).select("name").rdd.flatMap(lambda x: x).collect()

# Filtering can also be applied to string
df = df.where(df.name.startswith("h"))
df = df.where(df.name.endswith("r"))
df = df.where(df.name.contains("r"))

```

## FILTER Clause
Similar to `WHERE` clause
https://sparkbyexamples.com/pyspark/pyspark-where-filter/
```py
import pyspark.sql.functions as F
# Equal
df.filter(df.state == "OH")
df.filter(F.col("state") == "OH")

# Negation
df.filter(df.state != "OH")
df.filter(~(df.state == "OH"))

# Multiple conditions
df.filter( (df.state == "OH") | (df.gender != "M") )

# Filter in a list
df.filter(df.state.isin(["OH","CA","DE"]))
df.filter(~df.state.isin(["OH","CA","DE"]))

# String searching
df.filter(df.state.startswith("N"))
df.filter(df.state.endswith("N"))
df.filter(df.state.contains("N"))

# String length
df.filter(F.length("name") > 5)

# List size
df.filter(F.size(F.col("available_sizes")) > 10)

# Regex
df.filter(df.name.like("%rose%"))
df.filter(df.name.rlike("(?i)^*rose$"))

```

### FILTER - Advanced
```py
# Finding element in array datatype
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import StringType, IntegerType, ArrayType
data = [
    (("James","","Smith"),["Java","Scala","C++"],"OH","M"),
    (("Anna","Rose",""),["Spark","Java","C++"],"NY","F"),
    (("Julia","","Williams"),["CSharp","VB"],"OH","F"),
    (("Maria","Anne","Jones"),["CSharp","VB"],"NY","M"),
    (("Jen","Mary","Brown"),["CSharp","VB"],"NY","M"),
    (("Mike","Mary","Williams"),["Python","VB"],"OH","M")
 ]

schema = StructType([
     StructField('name', StructType([
        StructField('firstname', StringType(), True),
        StructField('middlename', StringType(), True),
         StructField('lastname', StringType(), True)
     ])),
     StructField('languages', ArrayType(StringType()), True),
     StructField('state', StringType(), True),
     StructField('gender', StringType(), True)
 ])

spark = SparkSession.builder.appName("app_name").getOrCreate()
df = spark.createDataFrame(data = data, schema = schema)

from pyspark.sql.functions import array_contains
df.filter(array_contains(df.languages, "Java")).show()

# +----------------+------------------+-----+------+
# |name            |languages         |state|gender|
# +----------------+------------------+-----+------+
# |[James, , Smith]|[Java, Scala, C++]|OH   |M     |
# |[Anna, Rose, ]  |[Spark, Java, C++]|NY   |F     |
# +----------------+------------------+-----+------+

# Filtering nested struct
df.filter(df.name.lastname == "Williams")

```

## ORDER BY Clause
https://sparkbyexamples.com/pyspark/pyspark-orderby-and-sort-explained/
https://spark.apache.org/docs/3.1.1/api/python/reference/api/pyspark.sql.DataFrame.orderBy.html
```py
# Sorting only based on a column (defining if the sort should be in descending or ascending)
df.sort(df.age.desc())
df.sort("age", ascending=False)
df.orderBy(df.age.desc())

from pyspark.sql.functions import asc, desc
df.sort(asc("age"))

# Order by multiple columns
df.orderBy(desc("age"), "name")
df.orderBy(["age", "name"], ascending=[0, 1])
df.sort("age", "name")
df.sort(col("age"), col("name"))
df.orderBy(col("age").asc(), col("name").desc())

```
`.orderBy()` and `.sort()` can be used interchangeably, but `.orderBy()` is actually calling `.sort()`, so might as well just use `.sort()`

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
Another example
```py
data = [(1706082429568, "ABC-201", [
    {
        "value": {
            "name": "Normal",
            "$type": "EnumBundleElement"
        },
        "name": "Priority",
        "$type": "SingleEnumIssueCustomField"
    },
    {
        "value": {
            "name": "Git Review",
            "$type": "StateBundleElement"
        },
        "name": "Stage",
        "$type": "StateIssueCustomField"
    },
])]
schema = T.StructType([
    T.StructField("created", T.LongType(), True),
    T.StructField("idReadable", T.StringType(), True),
    T.StructField(
        "customFields",
        T.ArrayType(
            T.StructType([
                T.StructField("name", T.StringType(), True),
                T.StructField("$type", T.StringType(), True),
                T.StructField(
                    "value",
                    T.StructType([
                        T.StructField("name", T.StringType(), True),
                        T.StructField("$type", T.StringType(), True)
                    ]), True)
            ])), True)
])
self.df = self.spark.createDataFrame(data, schema)
```


## Converting PySpark Dataframe to Dict
https://stackoverflow.com/questions/41206255/convert-pyspark-sql-dataframe-dataframe-type-dataframe-to-dictionary
```py
list_persons = list(map(lambda row: row.asDict(), df.collect()))
# [{'id': 0, 'created_at': '2024-02-22'}, {'id': 1, 'created_at': '2023-12-23'}, {'id': None, 'created_at': '2024-01-15'}]
```

## Converting Nested PySpark Dataframe into Dict
https://spark.apache.org/docs/3.1.2/api/python/reference/api/pyspark.sql.Row.asDict.html
```py
row = df.collect()[0]
row.asDict(True)
```

## Converting whole PySpark Dataframe to Dict
```py
df.toPandas().to_dict(orient="records")
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

### Parallelize data into dataframe
```py
import pyspark.sql.functions as f

df = spark._sc.parallelize([
    [0, 1.0, 0.71, 0.143],
    [1, 0.0, 0.97, 0.943],
    [0, 0.123, 0.27, 0.443],
    [1, 0.67, 0.3457, 0.243],
    [1, 0.39, 0.7777, 0.143]
]).toDF(['col1', 'col2', 'col3', 'col4'])

df_new = df.withColumn(
    'tada',
    f.struct(*[f.col('col2').alias('subcol_1'), f.col('col3').alias('subcol_2')])
)

df_new.show()
+----+-----+------+-----+--------------+
|col1| col2|  col3| col4|          tada|
+----+-----+------+-----+--------------+
|   0|  1.0|  0.71|0.143|   [1.0, 0.71]|
|   1|  0.0|  0.97|0.943|   [0.0, 0.97]|
|   0|0.123|  0.27|0.443| [0.123, 0.27]|
|   1| 0.67|0.3457|0.243|[0.67, 0.3457]|
|   1| 0.39|0.7777|0.143|[0.39, 0.7777]|
+----+-----+------+-----+--------------+
```

### Creating a dataframe with array of nested column
```py
data = [([{"id": 1, "value": "a"}, {"id": 2, "value": "b"}],)]
schema = T.StructType([
    T.StructField(
        "tasks",
        T.ArrayType(
            T.StructType([
                T.StructField("id", T.IntegerType(), False),
                T.StructField("value", T.StringType(), False),
            ])))
])

df = self.spark.createDataFrame(data, schema)
```

### Creating a dataframe with multiple columns where one of the column is an array of struct
```py
schema = T.StructType([
    T.StructField("id", T.StringType(), False),
    T.StructField(
        "teamOwnUsers",
        T.ArrayType(
        T.StructType([
            T.StructField("id", T.IntegerType(), False),
            T.StructField("type", T.StringType(), True),
        ])))
])
data = [("02f083d9", [{"id": 1, "type": "user"}, {"id": 2, "type": "user"}],)]
df_youtrack_projects = spark.createDataFrame(
    map(lambda x: Row(id = x[0], teamOwnUsers=x[1]), data), schema)
```

### Get the dictionary from PySpark Dataframe
```py
json_data = df.toPandas().to_dict(orient='records')
```

### Replace all nan value to None
```py
# Create a new dataframe
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 2, 3, 4],
    'C': [1, 2, 3, 4]
})
json_data = df.toPandas().replace({np.nan: None}).to_dict(orient="records")
```

### Creating a dataframe with only one nested column
```py
from pyspark.sql import Row
from pyspark.sql import types as T

# Create a dataframe using json data
data = [
    ((82510293, "Hard rubbish", "Waste Disposal Collection"),),
    ((12311231, "Dog grooming at home", "Mobile Pet Services"),),
]

schema = T.StructType([
    T.StructField(
        "tasks",
        T.StructType([
            T.StructField("id", T.LongType(), False),
            T.StructField("name", T.StringType(), False),
            T.StructField("carl_category_name", T.StringType(), False)
        ]))
])

df = spark.createDataFrame(data, schema)
# ^^^^^ Does not work even if we put double parenthesis
# as such ((82510293, "Hard rubbish", "Waste Disposal Collection"))
# Need to put another comma --------------------------------------v
# as such ((82510293, "Hard rubbish", "Waste Disposal Collection"),)
# because pyspark will reshape the dimension into a list when there
# is no other column (Refer: ## Creating nested pyspark dataframe with struct)

# Convert the data to a DataFrame
df = spark.createDataFrame(map(lambda x: Row(tasks=x), data), schema)

# Show the DataFrame
df.show()
```

### Creating a dataframe with struct only with selected columns (Reference only)
```py
from pyspark.sql import Row, SparkSession
import pyspark.sql.types as T

spark = SparkSession.builder.getOrCreate()

json_data = [
    ((82510293, "Hard rubbish", "Waste Disposal Collection")),
    ((12311231, "Dog grooming at home", "Mobile Pet Services")),
]

schema = T.StructType([
    T.StructField(
        "tasks",
        T.StructType([
            T.StructField("id", T.LongType(), False),
            T.StructField("name", T.StringType(), False),
        ])
    ),
    T.StructField("carl_category_name", T.StringType(), False)
])

# Convert the data to a DataFrame
df = spark.createDataFrame(
    map(lambda x: Row(tasks=x[:2], carl_category_name=x[2]), json_data),
    schema
)

# Show the DataFrame
df.show()
```

Example 2 (Reference only):
```py
import pyspark.sql.types as T
from pyspark.sql import Row, SparkSession

spark = SparkSession.builder.getOrCreate()

json_data = [
    ((82510293, "Hard rubbish", "Waste Disposal Collection")),
    ((12311231, "Dog grooming at home", "Mobile Pet Services")),
]

schema = T.StructType([
    T.StructField(
        "tasks",
        T.StructType([
            T.StructField("id", T.LongType(), False),
            T.StructField("carl_category_name", T.StringType(), False)
        ])
    ),
    T.StructField("name", T.StringType(), False)
])

# Convert the data to a DataFrame
df = spark.createDataFrame(
    map(lambda x: Row(tasks=Row(id=x[0], carl_category_name=x[2]), name=x[1]), json_data),
    schema
)

# Show the DataFrame
df.show()

+--------------------+--------------------+
|               tasks|                name|
+--------------------+--------------------+
|{82510293, Waste ...|        Hard rubbish|
|{12311231, Mobile...|Dog grooming at home|
+--------------------+--------------------+
```

### Another way of creating a new column with struct
```py
df = df.withColumn(
    "new_column_with_struct",
    F.struct("col_1", "col_2")
)
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
| Col1 | date_time                     | local_ts                   | timestamp_utc           |
| ---- | ----------------------------- | -------------------------- | ----------------------- |
| a    | 2020-09-08 14:00:00.917+02:00 | 2020-09-08 08:00:00.917-04 | 2020-09-08 12:00:00.917 |
| b    | 2020-09-08 14:00:00.900+01:00 | 2020-09-08 09:00:00.900-04 | 2020-09-08 13:00:00.9   |


## Convert timestamp to datetime
```py
# Without timezone
df.withColumn("date_time", F.to_date(F.from_unixtime(F.col("date_time") / 1000)))

# With timezone
df.withColumn("date_time", F.to_date(F.from_utc_timestamp((F.col("date_time") / 1000).cast(T.TimestampType()), "Asia/Kuala_Lumpur")))
```

## Update a columnd with updated value
https://sparkbyexamples.com/pyspark/pyspark-update-a-column-with-value/
```py
from pyspark.sql.functions import when
df3 = df.withColumn("gender", when(df.gender == "M","Male") \
      .when(df.gender == "F","Female") \
      .otherwise(df.gender))

# https://stackoverflow.com/questions/48389438/compare-two-columns-to-create-a-new-column-in-spark-dataframe
df.withColumn('flag', F.when((F.col("a") <= 2) | (F.col("b") <= 2), 1).otherwise(2)).show()

```

## Checking if the column data is null
```py
from pyspark.sql.functions import when

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

## Getting the distinct value in a list
```py
dfTaskResults.select("state").distinct().toPandas()["state"].tolist()
```

## Getting the list of raw values without the PySpark's row using flatMap
```py
# Method 1: rdd + flatMap
name_list = df.select("name").rdd.flatMap(lambda x: x).collect()

# Method 2: List comprehension
name_list = [row.name for row in df.select("name").collect()]
```

## Saving dataframe into csv
```py
# Option: CSV
df.write.csv("DATA_PATH")

# https://sparkbyexamples.com/spark/spark-write-dataframe-single-csv-file
# Option: Singular CSV
df.coalesce(1).write.csv("DATA_PATH")
df.repartition(1).write.csv("DATA_PATH")

```

## Saving dataframe into JSON
https://www.geeksforgeeks.org/dataframe-to-json-array-in-spark-in-python/
```py
# Into a folder list of json files
df.write.json("json_folder")

# Into a singular json in a folder
df.coalesce(1).write.json("data_merged")
df.repartition(1).write.json("data_merged")
```

## Saving dataframe into parquet
```py
# Option: Merging
df.write \
  .format("parquet") \
  .mode("append") \
  .option("mergeSchema", "true") \
  .save("DATA_PATH")

```

## Creating your schema manually
This is an optional script when you would like to manually set the datatype you want, often time, this is not needed because you can always use the mergeSchema option from pyspark to merge the schema which is fairly easy.
```py
df.write.format("parquet").mode("append").option("mergeSchema", "true").save(delta_directory)
```

But if you insist of manually setting it, below is the simple example:
```py
from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType
from pyspark.sql.types import StringType, LongType, DoubleType

SCHEMAS = {
    "user-engagement": {
        "newVsReturning": StringType,
        "dauPerWau": DoubleType,
        "engagedSessions": LongType,
    }
}

def create_schema(category):
  data_types = SCHEMAS.get(category, None)
  if data_types == None:
    raise NotImplementedError(f"Category is not implemented: {category}")

  return StructType([StructField(k, v(), True) for k, v in data_types.items()])

spark = SparkSession \
        .builder \
        .appName(dataSource) \
        .config("spark.driver.memory", "8g") \
        .config("spark.sql.legacy.timeParserPolicy", "LEGACY") \
        .config("spark.sql.caseSensitive", True) \
        .getOrCreate()

filepaths = ["../sample/data_1.json", "../sample/data_2.json"]

df_schema = create_schema("user-engagement")
df = (spark.read \
      .option("multiline",True) \
      .schema(df_schema) \
      .json(filepaths))
```

## Convert json string into struct
```py
from pyspark.sql import types as T
from pyspark.sql import functions as F

value_schema = T.StructType([
    T.StructField("ringId", T.StringType(), True),
    T.StructField("name", T.StringType(), True),
])

df = df.withColumn("value", F.from_json(df.value, value_schema))
df.show(truncate=False, vertical=True)
```

## Maths: SUM (+)
https://sparkbyexamples.com/pyspark/pyspark-sum/
```py
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("testing").getOrCreate()

simpleData = (("Java",4000,5), \
              ("Python", 4600,10), \
              ("Scala", 4100,15), \
              ("Scala", 4500,15), \
              ("PHP", 3000,20), \
             )
columns= ["CourseName", "fee", "discount %"]
df = spark.createDataFrame(data=simpleData, schema=columns)


from pyspark.sql.functions import sum
df.select(sum(df.fee)).show()

# Group and sum every column
df.groupBy("CourseName").sum().show()
# +----------+--------+---------------+
# |CourseName|sum(fee)|sum(discount %)|
# +----------+--------+---------------+
# |      Java|    4000|              5|
# |     Scala|    8600|             30|
# |       PHP|    3000|             20|
# +----------+--------+---------------+

# Group and only sum the selecte columns
df.groupBy("CourseName").sum("fee")
# +----------+--------+
# |CourseName|sum(fee)|
# +----------+--------+
# |      Java|    4000|
# |     Scala|    8600|
# |       PHP|    3000|
# +----------+--------+
```

## Separate Struct into individual column
Sometimes, when the schema of a column is not array, we cannot use explode, but we have to separate the internal struct into individual column sometimes
Example data
```py
+-------+-----------+--------------------+----+--------------------+---------+--------------------+
|  $type|description|              leader|name|              ringId|shortName|                team|
+-------+-----------+--------------------+----+--------------------+---------+--------------------+
|Project|       null|{User, d3f521f0-6...|abcd|da1a3245-76a7-4e9...|      abc|{UserGroup, abcd ...|
+-------+-----------+--------------------+----+--------------------+---------+--------------------+

# Schema
root
|-- $type: string (nullable = true)
|-- description: string (nullable = true)
|-- leader: struct (nullable = true)
|    |-- $type: string (nullable = true)
|    |-- ringId: string (nullable = true)
|-- name: string (nullable = true)
|-- ringId: string (nullable = true)
|-- shortName: string (nullable = true)
|-- team: struct (nullable = true)
|    |-- $type: string (nullable = true)
|    |-- name: string (nullable = true)
|    |-- ringId: string (nullable = true)
|    |-- usersCount: long (nullable = true)
```

To seperate them:
```py
def _get_camel_case(self, column_name):
  final_column_name = ""
  words = column_name.split()

  if len(words) == 1:
      if column_name == column_name.upper():
          return column_name
      else:
          return column_name[0].lower() + column_name[1:]

  for word in words:
      final_column_name += word if word == word.upper() else word.title()

  if words[0] != words[0].upper():
      final_column_name = final_column_name[0].lower() + final_column_name[1:]

  return final_column_name

def _get_combined_camel_case(self, column_name, nested_field_name):
  nested_field_name = self._get_camel_case(nested_field_name)
  nested_field_name = nested_field_name[0].upper() + nested_field_name[1:]
  column_name = self._get_camel_case(column_name)
  return f"{column_name}{nested_field_name}"

def _separate_struct(self, df, column, add_prefix):
  for nested_field in df.select(f"{column}.*").schema.fields:
    if (not nested_field.name.startswith("$") and
        nested_field.name != "type"):
      if add_prefix:
        column_name = self._get_combined_camel_case(column, nested_field.name)
      else:
        column_name = nested_field.name
      df = df.withColumn(column_name, df[f"{column}.{nested_field.name}"])
  df = df.drop(column)
  return df

def _explode_array_columns(self, df: DataFrame) -> DataFrame:
  for field in df.schema.fields:
    if (isinstance(field.dataType, T.ArrayType) and
        field.name not in self.ARRAY_COLUMN_NO_EXPLODE):
      df = df.withColumn(field.name, F.explode(field.name))
  return df

def _check_and_separate_struct(self, df: DataFrame) -> DataFrame:
  for field in df.schema.fields:
    if isinstance(field.dataType, T.StructType):
      add_prefix = field.name not in self.COLUMN_WITHOUT_PREFIX
      df = self._separate_struct(df, field.name, add_prefix)
  return df
```

Final result:
```
-RECORD 0-------------------------------
 $type          | Project
 description    | null
 name           | 10+3
 ringId         | da1a3245-76b7-4e9...
 shortName      | 103
 leaderRingId   | d3f521f0-6633-4e7...
 teamName       | 10+3 Team
 teamRingId     | 12eadb31-12b4-4f0...
 teamUsersCount | 28
```

## Pivot
### Group by 1 column
```py
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Sample data
data = [("Jill", "Marketing", 1000),
        ("Jill", "Sales", 2000),
        ("Jack", "Marketing", 3000),
        ("Jack", "Sales", 4000)]

# Create DataFrame
df = spark.createDataFrame(data, ["Name", "Department", "Revenue"])

# Pivot DataFrame
pivotDF = df.groupBy("Name").pivot("Department").sum("Revenue")

# Show pivoted DataFrame
pivotDF.show()

+----+---------+-----+
|Name|Marketing|Sales|
+----+---------+-----+
|Jack|     3000| 4000|
|Jill|     1000| 2000|
+----+---------+-----+
```

### Group by multiple columns
```py
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Sample data
data = [("Jill", "Marketing", 1000, "Q1"),
        ("Jill", "Sales", 2000, "Q1"),
        ("Jack", "Marketing", 3000, "Q1"),
        ("Jack", "Sales", 4000, "Q1"),
        ("Jill", "Marketing", 1500, "Q2"),
        ("Jill", "Sales", 2500, "Q2"),
        ("Jack", "Marketing", 3500, "Q2"),
        ("Jack", "Sales", 4500, "Q2")]

# Create DataFrame
df = spark.createDataFrame(data, ["Name", "Department", "Revenue", "Quarter"])

+----+----------+-------+-------+
|Name|Department|Revenue|Quarter|
+----+----------+-------+-------+
|Jill| Marketing|   1000|     Q1|
|Jill|     Sales|   2000|     Q1|
|Jack| Marketing|   3000|     Q1|
|Jack|     Sales|   4000|     Q1|
|Jill| Marketing|   1500|     Q2|
|Jill|     Sales|   2500|     Q2|
|Jack| Marketing|   3500|     Q2|
|Jack|     Sales|   4500|     Q2|
+----+----------+-------+-------+

# Pivot DataFrame
pivotDF = df.groupBy("Name", "Quarter").pivot("Department").sum("Revenue")

# Show pivoted DataFrame
pivotDF.show()

+----+-------+---------+-----+
|Name|Quarter|Marketing|Sales|
+----+-------+---------+-----+
|Jack|     Q1|     3000| 4000|
|Jill|     Q1|     1000| 2000|
|Jack|     Q2|     3500| 4500|
|Jill|     Q2|     1500| 2500|
+----+-------+---------+-----+
```

### Filling null values
https://sparkbyexamples.com/pyspark/pyspark-fillna-fill-replace-null-values/
```py
columns_to_fill = ["city", "type"]
df = df.fillna(value="abc", subset=columns_to_fill)
df.na.fill(value=123)
df.na.fill({"city": "unknown", "type": ""})
```

### JOINS
https://www.projectpro.io/article/pyspark-joins-for-data-analysis-by-example/564#mcetoc_1fsdoe8mdd
| Join Type            | PySpark Code                         | Description                                                                                                                                            |
| -------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Inner Join (DEFAULT) | `df3 = df1.join(df2, "id", "inner")` | Returns rows that have matching values in both dataframes.                                                                                             |
| Left Join            | `df3 = df1.join(df2, "id", "left")`  | Returns all rows from the left dataframe, and the matched rows from the right dataframe. If there is no match, the result is `null` on the right side. |
| Right Join           | `df3 = df1.join(df2, "id", "right")` | Returns all rows from the right dataframe, and the matched rows from the left dataframe. If there is no match, the result is `null` on the left side.  |
| Full Outer Join      | `df3 = df1.join(df2, "id", "outer")` | Returns all rows from both dataframes, and fills in `null` for missing matches on either side.                                                         |

### Upcoming notes
https://stackoverflow.com/questions/42983444/filtering-rows-with-empty-arrays-in-pyspark
https://sparkbyexamples.com/pyspark/convert-pyspark-dataframe-column-to-python-list/
https://sparkbyexamples.com/pyspark/pyspark-convert-array-column-to-string-column/
https://linuxhint.com/pyspark-data-preprocessing/
https://stackoverflow.com/questions/58310246/how-to-concatenate-to-a-null-column-in-pyspark-dataframe
https://stackoverflow.com/questions/44667565/pyspark-dataframe-changing-two-columns-at-the-same-time-based-on-condition
https://stackoverflow.com/questions/73746974/pyspark-prevent-column-value-from-changing-once-calculated
https://spark.apache.org/docs/3.1.1/api/python/_modules/pyspark/sql/dataframe.html#DataFrame.checkpoint
https://stackoverflow.com/questions/37332434/concatenate-two-pyspark-dataframes
https://www.programmingfunda.com/how-to-convert-pyspark-row-to-dictionary/
https://archive.is/UbMmY (Using pyarrow.parquet to read the internal stats of the data)