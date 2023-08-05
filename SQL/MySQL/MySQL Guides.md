# MySQL Quick Refresh

## Getting the current date / today's date
```sql
SELECT CURDATE();
```

## Compare the date diff
```sql
SELECT DATEDIFF(CURDATE(), CreatedAt) AS DayDiff from UpdatedDetails
ORDER BY CreatedAt DESC LIMIT 1;
```

## Take only the first few rows
```sql
SELECT ... LIMIT 10
```

## Adding table and data
```sql
CREATE TABLE sample_table_new (
    id INT NOT NULL,
    name VARCHAR(50),
    age INT
) DISTRIBUTED BY HASH(ID) BUCKETS 10 PROPERTIES('replication_num' = '1');

INSERT INTO sample_table_new (id, name, age)
VALUES (1, 'John Doe', 30),
       (2, 'Jane Smith', 25),
       (3, 'Michael Johnson', 40);
```