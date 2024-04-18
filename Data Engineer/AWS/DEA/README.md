# Section 1: Introduction

## Materials
| Title           | Link                                                                                    |
| --------------- | --------------------------------------------------------------------------------------- |
| Main webpage    | https://www.sundog-education.com/aws-data-engineer/                                     |
| Course material | https://dw9ne0o7jcasn.cloudfront.net/AWSDataEngineer/dea-materials.zip                  |
| Course slide    | https://dw9ne0o7jcasn.cloudfront.net/AWSDataEngineer/AWSCertifiedDataEngineerSlides.pdf |

# Section 2: Data Engineering Fundamentals
## Types of Data
### Structured
Definition: Data that is organized in a defined manner or schema, typically found in relational databases.

Characteristics:
- Easily queryable
- Organized in rows and columns
- Has a consistent structure

Examples:
- Database tables (Oracle, Redshift, PostgreSQL, MySQL)
- CSV files with consistent columns
- Excel spreadsheets

### Unstructured
Definition: Data that does not have a predefined structure or schema.

Characteristics:
- No predefined structure
- Come in various formats (text, images, audio, video, etc.)
- Can be difficult to query without preprocessing

Examples:
- Text files without a fixed format
- Videos and audio files
- Images
- Emails and word processing documents

### Semi-Strctured
Definition: Data that has structure in the form of tags, hierarchies but is not as organized as structured data.

Characteristics:
- Elements are tagged
- More flexible than structured data
- Less chaotic than unstructured data

Examples:
- JSON
- XML
- HTML
- Log files with formats (Need parsing to extract the data)
- Email headers (With structured fields like `To`, `From`, `Subject`, etc.)

## Properties of Data
### Volume
Definition: The amount of data that is being dealt at a given time

Characteristics:
- Measured in bytes, kilobytes, megabytes, gigabytes, terabytes, petabytes, exabytes, zettabytes, yottabytes
- The volume of data is growing at an exponential rate
- Big data is a term used to describe data that is too large to be processed by traditional methods
- Challenges arised when storing, processing, and analyzing high volumes of data

Examples:
- Social media data (video, image, post)
- Years of transaction data

### Velocity
Definition: The speed at which data is being generated, collected and processed

Characteristics:
- Kineses data streams or Kineses firehose are used to collect and process data in real-time for rapid ingestion
- Data is generated, processed at a high velocity

Examples:
- Stock market data (High frequency trading system where milliseconds matter)
- Sensor data from IoT streaming readings every millisecond

### Variety
Definition: The different types, sources and strucuture of data that are being dealt with

Characteristics:
- Data can come in various formats (structured, unstructured, semi-structured)
- Comes in multiple sources (databases, files, logs, social media, etc.)

Examples:
- Structured data: Database tables
- Unstructured data: Images, videos, audio, email
- Semi-structured data: JSON logs
- Healthcare data: Patient records, lab results, from electronic medical records, wearable devices, etc.

## Data Warehouse vs Data Lake
### Data Warehouse
Definition: A centralized repository for storing and managing structured data from one or more sources.

Characteristics:
- ETL (Extract, Transform then Load): Schema is determined before saving the data
- Schema-on-write: Schema is defined before writing the data
- Preprocess first before saving the data
- Legacy approach to data engineering
- Structured format
- Designed for complex query and analysis
- Typically used star or snowflake schema
- Optimized for read-heavy workloads

Examples:
- Amazon Redshift (Before this exist, giant Oracle database is used and it is expensive and hard to maintain)
- Google BigQuery
- Snowflake
- Microsoft Azure SQL Data Warehouse

```
Clickstream data -------+                         +---> Accounting data mart
                        |    +----------------+   |
Purchase data ----------+--->| Data Warehouse |---+---> Analysis data mart
                        |    +----------------+   |
Catalog data -----------+                         +---> Machine learning data mart
```
The data warehouse above has different views for different kind of applications / queries

### Data Lake
Definition: A centralized repository that allows you to store all your structured, semi-structured, unstructured data at any scale.

Characteristics:
- ELT (Extract, Load then Transform): Schema is determined after saving the data
- Schema-on-read: Schema is defined at the time of reading the data
- Store large amount of raw data without predefining the schema
- Do not preprocess the data before saving it, if we do, it is minimal only
- This support batch, real-time and stream processing
- Can be queried for data transformation and exploration
- Throw all the data into the lake and then figure out what to do with it later
- Mainly just to store the raw data, we only transform the data when we need it
- Data is always in raw format and never replicate the data, we just store it in the data lake S3

Examples:
- Amazon S3 (Simple Storage Service) when used as a data lake
- Google Cloud Storage
- Microsoft Azure Data Lake Storage
- Hadoop Distributed File System (HDFS) (This is the first data lake and it is hard to maintain, but it is not as popular as the cloud storage)

Flow:
1. Amazon S3
2. AWS Glue (ELT: To extract a structure and schema from the unstructured data)
3. Amazon Athena (Use Glue data catalog to figure out what the strucuture of the data is and how to query it: SQL query engine)
4. Amazon QuickSight (BI tool)

### Comparison between Data Warehouse and Data Lake
| Item         | Data Warehouse                                                      | Data Lake                                                                                       |
| ------------ | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Method       | ETL (Extract, transform then only load them into the system)        | ELT (Extract, load them into the system then only transform the data when we want to use them   |
| Method       | Define schema before writing to disk                                | Define schema at the time of reading the data                                                   |
| Method       | Schema-on-write                                                     | Schema-on-read                                                                                  |
| Method       | Preprocess first                                                    | Store raw data first                                                                            |
| Data type    | Structured                                                          | Structured, semi-structured, unstructured                                                       |
| Schema       | Star or snowflake schema                                            | No schema                                                                                       |
| Main purpose | For complex query (Expensive)                                       | Query for data transformation and exploration                                                   |
| Main purpose | Optimized for read-heavy workloads (Expensive)                      | Support batch, real-time and stream processing                                                  |
| Agility      | Less agile because predefined schema                                | More agile because because it accepts raw data without predefined schema, can transform anytime |
| Cost         | Expensive                                                           | Cheaper, but can rise up fast when processing large amounts of data                             |
| Maintenance  | Hard to maintain (Involve downtime when big project data migration) | Easier to maintain                                                                              |

### Which to choose?
| Choose         | When                                                                                                |
| -------------- | --------------------------------------------------------------------------------------------------- |
| Data Warehouse | You have structured data and require fast and complex queries + analysis                            |
| Data Warehouse | Data warehouse typically ingest data from different sources, otherwise it is database               |
| Data Warehouse | Mainly for business intelligence and analytics are the primary use case                             |
| Data Lake      | Mix of structured, semi-strucured and unstructured data                                             |
| Data Lake      | Need a scalable and cost effective solution to store a lot of data                                  |
| Data Lake      | Future needs of data is uncertain, therefore you want flexibility in storing and accessing the data |
| Data Lake      | Mainly for advanced analytics, machine learning, data discovery system                              |

### Data Lakehouse
Definition: Hybrid data architecture that combines the best features of both data lakes and data warehouses

Characteristics:
- Aims to provide the best performance, reliability and capabilities of data warehouse while maintaining the flexibility and scalability of a data lake
- Supports both structured and unstructured data
- Allows for schema-on-read and schema-on-write
- Provides capabilities for both detailed analytics and machine learning tasks
- Built on top of cloud or distributed architecture
- Benefits from Delta Lake, a open-source storage layer that brings ACID (Atomicity, Consistency, Isolation, Durability) transactions to Apache Spark and big data workloads
- ACID is for data integrity, it is a set of properties that guarantee that database transactions are processed reliably

Examples:
- AWS Lake Formation (with S3 and Redshift Spectrum - querying data in S3)
- Delta Lake - Built on top of Apache Spark (Open-source storage layer that brings ACID transactions to Apache Spark and big data workloads)
- Databricks Lakehouse Platform (Unified platform that combines the best of data lakes and data warehouses)
- Snowflake (Data Cloud)
- Azure Synapse Analytics (Analytics service that combines big data and data warehousing)

## Data Mesh
Definition: A new approach to data architecture that focuses on decentralizing data ownership and management to the domain level

Characteristics:
- It is not about technology, but about organizational and management design (How you structure the access and ownership of data within the large organization)
- More about data governance and data ownership
- Main idea: Individual teams own their own data, and they are responsible maintaining and managing their own data and also offering it as a data product to other teams
- Domain-based data management
- How is the data distributed and how is the data managed

## ETL Pipeline
Definition: A set of processes that extract data from one system, transform it and load it into data warehouse or data lake
ETL: Extract, Transform, Load to data warehouse
ELT: Extract, Load, Transform to data lake

### Extract
- Can be from source systems (databases, customer relationship management, flat files, APIs, logs, data repositories)
- Ensure data integrity and consistency during extraction (What happends if one of the API is corrupted, do we retry it, and how often will we retry it)
- Real-time or batch extraction (depending on the requirement)

### Transform
- Convert extracted data into suitabnle format before loading into target data warehouse
- Various operations:
  - Data cleansing (Remove duplication, correct the corrupted data)
  - Data enrichment (Add more data to the existing data from other sources)
  - Formatting (Data formatting, string manipulation, date formatting)
  - Aggregation (Summarize the data, group by, count, average)
  - Encoding (Convert data into different encoding format)
  - Decoding (Convert data from different encoding format to human readable format)
  - Handling null values (Reject all the rows with null values? Replace null values with default values? Or just keep the null values)

### Load
- Load the transformed data into the target data warehouse or another data repository
- Can be real-time (streaming manner) or batch loading
- Must ensure data integrity and consistency during loading

### Pipeline Management
- AWS Glue (Automatically do ETL or ELT when data is received)
- Process must be automated in reliable way
- Monitoring and logging (Monitor the pipeline, log the pipeline, alert when the pipeline is down)
- Orchestration services
  - EventBridge
  - Amazon Managed Workflows for Apache Airflow [Amazon MWAA]
  - AWS Step Functions
  - Lambda
  - Glue Workflows

## Common Data Sources and Data Formats
### Data Sources
- JDBC (Relational databases)
  - Java Database Connectivity
  - Platform-independent
  - Database-independent
  - Connectivity-independent
  - Language-dependent (Require Java coding to access the data)
- ODBC (Relational databases)
  - Object Database Connectivity
  - If you are not using Java, this is an intermediary layer
  - Platform-dependent (Need specific driver to access your database with ODBC)
  - Language-independent (Because not built explicitly on Java)
- Raw Logs
- APIs
- Streams (Some data sources provide your data in real time as it's received)
  - Kafka
  - Kinesis

### Common Data Formats
1. CSV (Common-Separated Values)
   - Text-based format
   - Data in tabular form where each line is a row and each values are separated with a separator/delimiter (comma, tab, etc.)
   - TSV file stands for Tab-Separated Values
   - When to use:
     - Small to medium-sized data
     - Data is simple and does not have complex structure
     - Data is not sensitive
     - Data interchange between systems with different technologies (Many systems can handle CSV)
     - Human-readable and editable data storage (Easier to read)
     - Importing and exporting data from databases and spreadsheets
     - Do not require encoding and decoding
   - Systems:
     - Databases (SQL-based)
     - Excel
     - Pandas
     - R

2. JSON (JavaScript Object Notation)
   - Text-based format
   - Lightweight
   - Human-readable data interchange format
   - Data is in key-value pairs
   - Data is in a hierarchical structure
   - When to use:
     - Data interchange between web server and web client
     - Config and settings for software application
     - Want a flexible schema and nested data structure
   - Systems:
     - Web browsers
     - RESTful APIs
     - NoSQL databases (MongoDB, CouchDB)
     - JavaScript
     - Python
     - Java

3. Avro (Apache Avro)
   - For evolving schema and high compatibility, Avro should be chosen for downstream analytics
   - Binary format with both schema and data
   - Compact, fast and efficient
   - Data serialization system
   - Data is in a schema
   - When to use:
     - Big data systems (Hadoop, Kafka, Spark, Hive, Pig)
     - Real-time data processing
     - Schema change is frequent (change in data structure) [This is the real use case because there is no point of saving the fixed schema]
     - Efficient for serialization and deserialization (Faster than JSON) for data transport between two systems because it is binary nature and the information of how it is decoded is also included in the format as well
   - Systems:
     - Hadoop
     - Apache Kafka
     - Apache Spark
     - Apache Flink

4. Parquet
   - Columnar storage format (optimized for analytics) instead of row-based storage
   - Binary format
   - Efficient for analytics (When doing query, we often only interested in the specified column instead of row)
   - Efficient compression and encoding schemes (Column is in a same format, allow easy compression and encoding)
   - When to use:
     - Big data systems (Hadoop, Spark, Hive, Impala)
     - Analyze large datasets
     - Reading specified columns instead of entire rows
     - Storing data on distributed system where I/O operations and storage required optimization because with parquer, we can split things out based on the columns which are being queried, maybe I want to store some columns on different server. Trying to minizise the overhead of the I/O operations / storage
     - Efficient for analytics
     - Efficient for query performance
     - When we have alot of columns but we only want to query a few columns
   - Systems:
     - Hadoop
     - Apache Spark
     - Apache Hive
     - Apache Impala
     - AWS Redshift Spectrum

5. XML (eXtensible Markup Language)
   - Text-based format
   - Human-readable
   - Data is in a hierarchical structure
   - When to use:
     - Data interchange between web server and web client
     - Config and settings for software application
     - Want a flexible schema and nested data structure
   - Systems:
     - Web browsers
     - RESTful APIs
     - NoSQL databases (MongoDB, CouchDB)
     - JavaScript
     - Python
     - Java


## Data Modelling
1. Star Schema
- Fact table in the middle
- Dimension tables surrounding the fact table
- Foreign keys in the fact table
- Primary keys in the dimension tables
- Below shows the ERD (Entity Relationship Diagram)

```
 +------------+                 +-------------+
 | Dim_Course |                 | Dim_Student |
 +------------+                 +-------------+
 | CourseID   |                 | StudentID   |
 | Name       |                 | Name        |
 | Summary    |                 | Address     |
 | Instructor |                 | Email       |
 | Price      |                 | Class       |
 +------------+                 +-------------+
       |                               |
       +---------------+---------------+
                       |
              +-----------------+
              | Fact_Enrollment |
              +-----------------+
              | CourseID        |
              | StudentID       |
              | PaymentID       |
              | Date            |
              +-----------------+
                       |
                +-------------+
                | Dim_Payment |
                +-------------+
                | PaymentID   |
                | PaymentType |
                | Amount      |
                +-------------+
```

## Data Lineage
Definition: Visual representation that shows the flow and transformation of data through its lifecycle from its origin to its final destination

Characteristics:
- Some sort of records of what is done to the data along the way of the transformation
- Why do we need this? When there is problem, we can track back to troubleshoot the problem
- This is require for compliance and auditing purposes where data is really sensitive or secure data when you are dealing with law
- Gives a clear understanding of the data flow and transformation, and consumed within the system
- Data lineage can be created using Spline agent (Apache Spark tool) attached to Glue
- Ingesting data using AWS Glue from S3
- Glue is transporting data from S3 raw data into Glue Data Catalog, Spline agent attached to Glue is capturing what it is doing along the way, it has the Lineage API (Alternative: SageMaker Lineage)
- Using AWS Lambda to consume the lineage data information from Spline and then writing into Amazon Neptune (Graph database) to visualize the data lineage, then we can query the Amazon Neptune to see the data lineage

## Schema Revolution
Definition: Ability to adapt and change the schema of a dataset over time without disrupting the existing process or systems (Like data lake where we can change the schema on the fly)

Importance:
- Ensure data system can adapt to new changes according to business requirements (Happens alot and we don't want to go back and deal with data migration every time we change the schema)
- Allow for flexibility and agility in data management (Addition, removal, modification of fields)
- Maintain backward compatibility with older data records

Example:
- Glue Schema Registry (AWS Glue DataBrew) - Schema discovery, compatibility, validation, registration
- So that Glue can manage different versions of the schema over time and ensure backward compatibility with older data records

## Database Performance Optimization
- Optimization techniques and tools that make the database perform faster and more efficiently

1. Indexing
- Avoid full table scans
- Understand what indexes you can build to make sure that we can access the data we need quickly
- Enforce data uniqueness and integrity (Primary key, unique key)

2. Partitioning
- Divide large tables into smaller and more manageable pieces
- Reduce the amount of data that needs to be scanned (Eg: Partition by date, region, etc.)
- Enable parallelism and improve query performance
- Helps with data lifecycle management (If we are partitioning based on time, we can take those older partitions and move them to a cheaper storage or archive them)

3. Compression
- Speed up data transfer and reduce storage usage and disk reads
- Lot of the time, database is held back by disk I/O, so if we can compress the data, we can read more data at once
- Common compression format which is supported by Amazon Redshift (LZOP, Zstandard - ZSTD, BZIP2, GZIP)
- All of the format comes with different trade-offs (Compression ratio, speed of compression, speed of decompression) Avoid going from IO bound to CPU bound because the compression format is too complicated
- Columnar compression (Example: Parquet, ORC)

## Data Sampling Techniques
Definition: Process of selecting a subset of data from a larger dataset to gain insights and make inferences about the larger dataset

Why?
- Large datasets can be time-consuming and resource-intensive to process
- Sampling can be used to test hypothesis, validate models, and make predictions
- Sampling can be used to understand the characteristics of the larger dataset

### Random Sampling
- Each item in the dataset has an equal chance of being selected
- Only works when the data is not sorted

### Stratified Sampling
- Choose this instead of random sampling when have large dataset but have different classification within the dataset
- Divide the population into homogeneous subgroups (strata) and then take a random sample from each stratum
- Ensure that we have good representation from each stratum (subgroup), don't need to worry about missing an entire category
- Example: Selecting a same amount of students from each grade level

### Systemic Sampling
- Select a random starting point and then select every nth item in the population
- Example: Select every 10th person in a list of names
- Ensure that we are not missing any data

### Cluster Sampling
- Divide the population into clusters and then randomly select some of the clusters
- Example: Selecting a random sample of schools and then surveying all the students in those schools
- Useful when the population is large and spread out
- Useful when the population is in a cluster, group, community, region

### Convenience Sampling
- Selecting a sample that is convenient to access
- Example: Surveying people in a shopping mall
- Not a good representation of the population, dataset

### Judgmental Sampling
- Selecting a sample based on the judgment of the researcher
- Example: Selecting a sample of people who are known to have a particular characteristic
- Not a good representation of the population, dataset

## Data Skew Mechanisms
Definition: Imbalance in the distribution of data across partitions or nodes in a distributed system
- Problem: In a distributed database, some nodes may have more data than others, causing performance issues
- Sometimes we call this celebrity problem where one node is getting all the data and it is getting overwhelmed
- Partitioning is a data optimization technique that divides large tables into smaller and more manageable pieces so we can process them in parallel
- But partitioning does not work when data is not evenly distributed / incoming traffic is uneven
- Example: In IMDB, Tom Cruise has a lot of movies, so the whatever partition he is mapped to, will have alot more traffic than some other actor in films from 30 years ago

### Consequences
- Non-uniform data distribution
- Partitioning strategy is inadequate / inefficient
- Temporal skew (Data is skewed based on time, data partitioned 5 years ago is much smaller than data partitioned today, where most recent partition is way larger than older partition)
- Performance degradation

### Solutions
- Monitor data distribution and create alert when data skew is detected (CloudWatch)
- Adaptive partitioning
  - Dynamically adjust the partition based on the observed distribution over time
  - Automatically repartitioning in real time based on the data distribution
  - Example: If we know that the data is skewed based on the date, we can partition the data based on the date
  - How: We can use the AWS Glue to do the adaptive partitioning
- Salting
  - Add a random number to the partition key to distribute the data more evenly
  - Example: If we know that the data is skewed based on the user ID, we can add a random number to the user ID
- Repartitioning periodically (very destruptive)
  - Very distruptive: Go back and reshuffle all the data while you are still trying to read the data (Try to avoid)
  - Manually repartition the data based on the skewness of the data
  - Example: If we know that the data is skewed based on the region, we can repartition the data based on the region
- Sampling
  - Sample the data and analyze the distribution to identify the skewness and adjust the partitioning accordingly
  - Example: If we know that the data is skewed based on the user ID, we can add a random number to the user ID
  - Part of adaptive partitioning
- Custom partitioning
  - Define custom rules and functions to partition the data based on the skewness
  - Example: We know upfront that Tom Cruise will have more data, he can have his own partition
  - Hacky method but it's a solution

## Data Validation and Profiling
- Data Validation: Process of ensuring that data is accurate, complete, and consistent
- Data Profiling: Process of examining datasets to understand their structure, content, relationships, and quality

### Data Validation
#### Data Completeness
- Definition: Ensure that all the required data is present
- Checks: Missing values, null counts, percentage of populated fields (Does this percentage fall within the acceptable range)
- Importance: Incomplete data can lead to inaccurate analysis and decision-making

#### Data consistency
- Definition: Ensure that data is consistent across different sources and systems, and they do not contradict/overlap each other
- Checks: Cross-field validation, comparing data from different sources/periods, duplicate records, conflicting data, data integrity constraints (Foreign key, unique key)
- Importance: Inconsistent data can lead to confusion and errors in analysis
- Example: One table with movie ratings from 1 - 5 and another table has a rating from 1 - 10, when we try to combine them, we will have confusion and incorect conclusion

#### Data Accuracy
- Definition: Ensure that data is accurate and free from errors, ensures data is correct, reliable and represent what it supposed to do
- Checks: Comparing with trusted sources, validation using known standards or rules, pass through sanity check (does the overall distribution of the data matches what we expect from the real world or not), data type validation, range validation, format validation, data integrity constraints
- Importance: Inaccurate data can lead to incorrect analysis and decision-making

#### Data Integrity
- Definition: Ensures data maintains its correctness and consistency over its lifecycle and across different systems
- Checks: Referential integrity (foreign key checks in database), relationship validation, entity integrity, domain integrity, business rules, data integrity constraints
- Importance: Ensure relationships between data are maintained and data is not corrupted, and data remain trustworthy over time

#### Difference between data accuracy and data integrity
https://www.ibm.com/blog/data-accuracy-vs-data-integrity/
- Data accuracy focuses on the correctness of data values, ensuring that they are free from errors and accurately represent real-world entities
- Data integrity refers to the consistency, reliability, and trustworthiness of data throughout its lifecycle.
- Data accuracy is primarily concerned with identifying and eliminating errors in data values, such as transcription mistakes, duplicate entries, and incorrect values.
- Data integrity is concerned with maintaining the accuracy and consistency of data over time, even as it is transferred between systems or manipulated for various purposes.

##### Methods to ensure data accuracy
- Data validation: This involves implementing predefined rules or algorithms to detect errors, inconsistencies, and inaccuracies in data. It can be done at the time of data entry or afterward.
- Data cleansing: This involves identifying and correcting (or removing) errors and inconsistencies in datasets. It often includes removing duplicates, correcting misspellings, and standardizing data.
- Data profiling: It involves examining datasets to identify patterns, trends, and anomalies. These insights can be used to detect potential inaccuracies or inconsistencies.

##### Methods to ensure data integrity
- Access controls: These are used to prevent unauthorized access to data. Access controls can include usernames and passwords, encryption, and network firewalls.
- Backups and recovery: Regular backups are crucial for maintaining data integrity. In the event of data loss or corruption, backups allow data to be restored to its original state.
- Error detection and correction techniques: These include checksums, cyclic redundancy checks, and digital signatures. These techniques are used to identify and correct errors that may have occurred during data transmission or storage.
- Data governance: Implementing strong data governance practices helps ensure data integrity by defining who is responsible for maintaining different aspects of data, including its accuracy, consistency, and reliability.

## SQL
### Aggregation
COUNT
```
SELECT COUNT(*) AS total_rows FROM employees;
```
SUM
```
SELECT SUM(salary) AS total_salary FROM employees;
```
AVG
```
SELECT AVG(salary) AS average_salary FROM employees;
```
MAX / MIN
```
SELECT MAX(salary) AS highest_salary FROM employees;
```

### Aggregation with CASE
Filter on one thing at a time using WHERE clauses after the aggregation
```
SELECT COUNT(*) AS high_salary_count
FROM employees
WHERE salary > 70000;
```
Filter on multiple things at once using CASE
```
SELECT
COUNT(CASE WHEN salary > 70000 THEN 1 END) AS high_salary_count,
COUNT(CASE WHEN salary BETWEEN 50000 AND 70000 THEN 1 END) AS medium_salary_count,
COUNT(CASE WHEN salary < 50000 THEN 1 END) AS low_salary_count
FROM employees;
```

### GROUP BY: Grouping
Definition: Split things up by a given field
Example: Count how many employees in a department
```
SELECT department_id, COUNT(*) AS employee_count
FROM employees
WHERE join_date > '2020-01-01'
GROUP BY department_id;
```

### GROUP BY: Grouping by multiple fields (Nested grouping)
```
SELECT YEAR(sale_date) AS sale_year, product_id, SUM(amount) AS total_sales
FROM sales
GROUP BY sale_year, product_id
ORDER BY sale_year, total_sales DESC;
```

### ORDER BY: Sorting
```sql
SELECT department_id, COUNT(*) AS employee_count
FROM employees
ORDER BY employee_count DESC;
-- ORDER BY employee_count ASC;
-- ORDER BY employee_count; -- same as ASC
```

### HAVING: Filtering after grouping
Definition: Filter the results that has been grouped using an aggregation
```
SELECT department FROM employees
GROUP BY department
HAVING COUNT(*) > 1;
```

### PIVOT: Transform rows into columns
Definition: Turning row-lvel data into columnar data
Example: Table with sales amounts and salesperson each row but we want to see the sales amount by salesperson
- Only works with SQL Server, Oracle, MySQL, PostgreSQL
```
SELECT salesperson, [Jan] AS Jan_sales, [Feb] AS Feb_sales
FROM
(SELECT salesperson, month, sales FROM sales) AS sourceTable
PIVOT
(
  SUM (sales)
  FOR month IN ([Jan], [Feb])
) AS PivotTable;
```
Output
```
| salesperson | Jan_sales | Feb_sales |
| ----------- | --------- | --------- |
| Alice       | 1000      | 2000      |
| Bob         | 1500      | 2500      |
```

- Without pivoting
```
SELECT
  salesperson,
  SUM(CASE WHEN month = 'Jan' THEN sales ELSE O END) AS Jan_sales,
  SUM(CASE WHEN month = 'Feb' THEN sales ELSE O END) AS Feb_sales
FROM sales
GROUP BY salesperson;
```

### When is the square bracket used?
1. When the column name has space
```
SELECT salesperson, [monthly sales] AS Jan_sales
FROM sales
```
2. When the column name is same as the SQL keyword
```
SELECT id, [user]
FROM users
```

### UNPIVOT: Transform columns into rows
Definition: Turning columnar data into row-level data
Example: Table with sales amount by month and we want to see the sales amount by month
- Only works with SQL Server, Oracle, MySQL, PostgreSQL
```
SELECT month, salesperson, sales
FROM
(SELECT salesperson, [Jan], [Feb] FROM sales) AS sourceTable
UNPIVOT
(
  sales FOR month IN ([Jan], [Feb])
) AS UnpivotTable;
```
Output
```
| month | salesperson | sales |
| ----- | ----------- | ----- |
| Jan   | Alice       | 1000  |
| Feb   | Alice       | 2000  |
| Jan   | Bob         | 1500  |
| Feb   | Bob         | 2500  |
```

### Table alias
Definition: Short name for a table
Example: Using table alias to simplify the query
```
SELECT e.name
FROM employees e
```

### JOIN: Combining data from multiple tables
#### INNER JOIN (Default join)
Definition: Return rows when the condition we are joining on exists in both tables
```
SELECT e.name, e.department_id, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id;
```
Output
```
| name  | department_id | department_name |
| ----- | ------------- | --------------- |
| Alice | 1             | Sales           |
| Bob   | 2             | Marketing       |
```

#### LEFT JOIN (Outer join)
Definition: Return all rows from the left table, and the matched rows from the right table
```
SELECT e.name, e.department_id, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id;
```
Output
```
| name  | department_id | department_name |
| ----- | ------------- | --------------- |
| Alice | 1             | Sales           |
| Bob   | 2             | Marketing       |
| Carol | 3             | NULL            |
```

#### RIGHT JOIN (Outer join)
Definition: Return all rows from the right table, and the matched rows from the left table
```
SELECT e.name, e.department_id, d.department_name
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.department_id;
```
Output
```
| name  | department_id | department_name |
| ----- | ------------- | --------------- |
| Alice | 1             | Sales           |
| Bob   | 2             | Marketing       |
| NULL  | NULL          | HR              |
```

#### FULL JOIN (Outer join)
Definition: Return all rows from left and right tables whether or not there is a match
- Normally use for data comparison and debugging
- To get a good picture when we have mismatched data where we do not have matching keys
```
SELECT e.name, e.department_id, d.department_name
FROM employees e
FULL JOIN departments d ON e.department_id = d.department_id;
```
Output
```
| name  | department_id | department_name |
| ----- | ------------- | --------------- |
| Alice | 1             | Sales           |
| Bob   | 2             | Marketing       |
| Carol | 3             | NULL            |
| NULL  | NULL          | HR              |
```

#### CROSS OUTER JOIN
Definition: Return all possible combinations between the two tables
```
SELECT e.name, d.department_name
FROM employees e
CROSS JOIN departments d;
```
Output
```
| name  | department_name |
| ----- | --------------- |
| Alice | Sales           |
| Bob   | Sales           |
| Carol | Sales           |
| Alice | Marketing       |
| Bob   | Marketing       |
| Carol | Marketing       |
| Alice | HR              |
| Bob   | HR              |
| Carol | HR              |
```

### UNION
Definition: Combine the result set of two or more SELECT statements
- UNION: Combine the result set of two or more SELECT statements, remove duplicates
- UNION ALL: Combine the result set of two or more SELECT statements, include duplicates
```
SELECT name FROM employees
UNION
SELECT name FROM contractors;
```

### INTERSECT
Definition: Return common rows between two SELECT statements
```
SELECT name FROM employees
INTERSECT
SELECT name FROM contractors;
```

### EXCEPT
Definition: Return rows that are in the first SELECT statement but not in the second SELECT statement
```
SELECT name FROM employees
EXCEPT
SELECT name FROM contractors;
```

### Subquery
Definition: Query within another query
```
SELECT name, department_id
FROM employees
WHERE department_id IN
(
  SELECT department_id
  FROM departments
  WHERE department_name = 'Sales'
);
```

### SQL Regular Expression
Definition: For pattern matching
Example
```sql
-- Select any rows where the name starts with 'fire' or 'ice' (case-insensitive)
SELECT * FROM name WHERE name ~*'^(fire|ice)';
```
| Symbol   | Description                                                             |
| -------- | ----------------------------------------------------------------------- |
| ~        | Regular expression operator (case-sensitive)                            |
| ~*       | Case-insensitive regular expression operator                            |
| !~*      | Not match expression, case-insensitive                                  |
| ^        | Caret - Match a pattern at start of the string                          |
| $        | Match a pattern at end of the string (boo$ will match boo but not book) |
| \|       | Alternation (OR) (sit\|sat matches both sit and sat)                    |
| []       | Any character inside the brackets                                       |
| [a-z]    | Matches any lower case letter between a and z                           |
| [a-z]{4} | Matches any lower case letter between a and z with 4 characters         |
| [^]      | Any character not inside the brackets                                   |
| [^a-z]   | Does not match any lower case letter between a and z                    |
| \d       | Matches any digit                                                       |
| \w       | Matches any letter, digit or underscore                                 |
| \s       | Matches any whitespace character                                        |
| \t       | Matches a tab character                                                 |
| .        | Any character                                                           |
| *        | Zero or more occurrences                                                |
| +        | One or more occurrences                                                 |
| ?        | Zero or one occurrence                                                  |

## SQL Coding Best Practices
1. Use meaningful table and column names
```sql
SELECT employee_name, department_name
FROM employees
```
2. Use consistent and clear formatting
```sql
SELECT
  employee_name,
  department_name
FROM
  employees
```
3. Use comments to explain complex queries
```sql
-- Get the total number of employees in each department
SELECT department_name, COUNT(*) AS employee_count
FROM employees
GROUP BY department_name;
```
4. Use aliases for tables and columns
```sql
SELECT e.employee_name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;
```
5. Use subqueries for complex queries
```sql
SELECT employee_name, department_name
FROM employees
WHERE department_id IN
(
  SELECT department_id
  FROM departments
  WHERE department_name = 'Sales'
);
```
6. Use UNION, INTERSECT, EXCEPT for combining results
```sql
SELECT name FROM employees
UNION
SELECT name FROM contractors;
```
7. Use JOIN for combining data from multiple tables
```sql
SELECT e.employee_name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;
```
8. Use GROUP BY for grouping data
```sql
SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY department_id;
```
9. Use ORDER BY for sorting data
```sql
SELECT department_id, COUNT(*) AS employee_count
FROM employees
ORDER BY employee_count DESC;
```
10. Use HAVING for filtering after grouping
```sql
SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 1;
```
11. Use CASE for conditional logic
```sql
SELECT
  employee_name,
  CASE
    WHEN salary > 70000 THEN 'High'
    WHEN salary BETWEEN 50000 AND 70000 THEN 'Medium'
    ELSE 'Low'
  END AS salary_category
FROM employees;
```
12. Use PIVOT and UNPIVOT for transforming data
```sql
SELECT salesperson, [Jan] AS Jan_sales, [Feb] AS Feb_sales
FROM
(SELECT salesperson, month, sales FROM sales) AS sourceTable
PIVOT
(
  SUM (sales)
  FOR month IN ([Jan], [Feb])
) AS PivotTable;
```
13. Use SQL Regular Expression for pattern matching
```sql
SELECT * FROM name WHERE name ~*'^(fire|ice)';
```
14. Use SQL functions for data manipulation
```sql
SELECT
  employee_name,
  UPPER(employee_name) AS uppercase_name,
  LOWER(employee_name) AS lowercase_name,
  LENGTH(employee_name) AS name_length
FROM employees;
```
15. Use SQL transactions for data integrity
```sql
BEGIN TRANSACTION;
INSERT INTO employees (employee_name, department_id) VALUES ('Alice', 1);
INSERT INTO employees (employee_name, department_id) VALUES ('Bob', 2);
COMMIT;
```
16. Use SQL views for reusable queries
```sql
CREATE VIEW employee_details AS
SELECT employee_name, department_name
FROM employees
JOIN departments ON employees.department_id = departments.department_id;
```
Using the view
```sql
SELECT * FROM employee_details;
```
17. Use SQL indexes for performance optimization
```sql
CREATE INDEX idx_employee_name ON employees (employee_name);
```
18. Use SQL constraints for data integrity
```sql
ALTER TABLE employees
ADD CONSTRAINT fk_department_id
FOREIGN KEY (department_id)
REFERENCES departments (department_id);
```
19. Use SQL triggers for automating tasks
```sql
CREATE TRIGGER update_salary
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
  INSERT INTO salary_history (employee_id, old_salary, new_salary)
  VALUES (OLD.employee_id, OLD.salary, NEW.salary);
END;
```
Using the trigger
```sql
UPDATE employees SET salary = 50000 WHERE employee_id = 1;
```
20. Use SQL stored procedures for reusable code
```sql
CREATE PROCEDURE get_employee_details
AS
BEGIN
  SELECT employee_name, department_name
  FROM employees
  JOIN departments ON employees.department_id = departments.department_id;
END;
```
Using the stored procedure
```sql
EXEC get_employee_details;
```

### SQL Exercises
1. Practicing aggregation queries in SQL
You probably know the story of the Titanic, an ocean liner that tragically sank in 1912. A famous policy of the time was "women and children first" when loading up the lifeboats in such a situation. Does the data show this is what actually happened on the Titanic? We've loaded up a sample of 100 passengers on the Titanic, which includes their age in years, whether they survived, and their self-reported gender, into a table named titanic. Explore this data, and compute:
- A listing of the first ten rows in the titanic table, to help you understand its structure and column names.
```sql
SELECT * FROM titanic LIMIT 10;
```
- The overall survival rate of the passengers in this data set. This result should be labeled overall_rate.
```sql
SELECT AVG(Survived) AS overall_rate FROM titanic;
```
- The overall survival rate of "women and children," identified by a gender of 'female' or age of 12 or younger. This result should be labeled women_children_rate.
```
SELECT AVG(Survived) AS women_children_rate FROM titanic
WHERE Sex == 'female' OR Age <= 12;
```
- The overall survival rate of everyone else who does not fit our definition of "women and children." This result should be labeled others_rate.
```sql
-- Using subquery
SELECT AVG(Survived) AS others_rate FROM titanic
WHERE PassengerId NOT IN (
  SELECT PassengerId FROM titanic
  WHERE Sex == 'female' OR Age <= 12
) AND Age IS NOT NULL; -- Due to the reason that there are data without age, we will exclude them

-- Using logic
SELECT AVG(Survived) AS others_rate FROM titanic
WHERE Sex == 'male' AND Age > 12;
```

2. Practicing grouping queries in SQL
Did class matter? We have the same sample of 100 passengers on the Titanic, but this time we want to explore if the passenger class of their ticket (first, second, or third class) affected their odds of survival.
- Your sample dataset is in a table named titanic. This contains a column named Survived, which is 1 if they survived and 0 if not. There is also a Pclass column indicating their passenger class (1, 2, or 3.)
- Your task is to use GROUP BY in SQL to produce the survival rate for each passenger class in our dataset. Your output should contain a table with two columns named Pclass and survival_rate. The results should be sorted in ascending order by passenger class.
```sql
SELECT Pclass, AVG(Survived) AS survival_rate FROM titanic
GROUP BY Pclass
ORDER BY Pclass;
```

3. Practicing join queries in SQL
We've loaded up a couple of tables of data from a fictional retailer: Products, containing information about the products sold by the company, and Suppliers, containing information about the companies that provided those products. These two tables are connected by columns named SupplierID.
- Create a report of every ProductName in the Products table, together with the CompanyName associated with each product's supplier.
This query should be written in such a way that every product is listed in your report, even if no match exists in the Suppliers table for its SupplierID. Your final results should be sorted alphabetically by ProductName.
```sql
SELECT p.ProductName, s.CompanyName
FROM Products p
FULL JOIN Suppliers s ON p.SupplierID = s.SupplierID
ORDER BY ProductName
```

# Section 3: Storage
## Amazon S3
Definition: Scalable, secure, durable, and highly available object storage service

Characteristics:
- Main building blocks of AWS
- Infinitely scalable
- Many websites uses S3 as a backbone
- It is used as an integration as well

Use Cases:
- Backup and storage
- Disaster recovery - Move data into another region and in case on side is going down, you have a backup
- Data archiving - Retrieve at later stage for much cheaper
- Hybrid cloud storage - Store data on-premises and in the cloud
- To host application
- To host media - Videos, images, etc.
- Data lake to store a lot of data to perform big data analytics
- Deliver software updates
- Static website hosting

Example:
- Nasdaq uses S3 to store 7 years of data into S3 Glacier (Archival service of Amazon S3)
- Sysco runs analytics on dat anad gain business insights

### Amazon S3 - Buckets
- Buckets can be seen as top level directory like root folder
- Files in S3 are called objects
