# MySQL Quick Refresh

## Getting list of databases
```sql
SHOW DATABASES;
```

## SELECT: Choosing the data
```sql
-- Return all columns and all rows
SELECT * FROM People;

-- Return only the specified columns
SELECT name, age FROM People;
```

## WHERE: Filtering data
```sql
SELECT name FROM People
WHERE age > 50;
```

## LIKE: String regex checking
```sql
SELECT name FROM People
WHERE name LIKE 'A%' -- Checking if the name is starting with 'A'
```


## LIMIT: Take only the first few rows
```sql
SELECT ... LIMIT 10
```

## OFFSET: Skip first few rows
```sq
SELECT ... OFFSET 10
```

## CREATE TABLE: Creating a new table
```sql
CREATE TABLE sample_table_new (
    id INT NOT NULL,
    name VARCHAR(50),
    age INT
) DISTRIBUTED BY HASH(ID) BUCKETS 10 PROPERTIES('replication_num' = '1');
```

## INSERT INTO: Adding data into table
### Adding single data
```sql
INSERT INTO sample_table_new(id, name, age)
VALUES (1, 'John Cena', 50)
```

### Adding multiple data
```sql
INSERT INTO sample_table_new (id, name, age)
VALUES (1, 'John Doe', 30),
       (2, 'Jane Smith', 25),
       (3, 'Michael Johnson', 40);
```

---

## CURDATE: Getting the current date / today's date
```sql
SELECT CURDATE();
```

## DATEDIFF: Compare the date diff
```sql
SELECT DATEDIFF(CURDATE(), CreatedAt) AS DayDiff from UpdatedDetails
ORDER BY CreatedAt DESC LIMIT 1;
```

## Checking if MySQL server is alive
```bash
mysqladmin ping -h 172.20.80.2 -P9030 -uroot -pYOUR_PASSWORD
```
