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
-