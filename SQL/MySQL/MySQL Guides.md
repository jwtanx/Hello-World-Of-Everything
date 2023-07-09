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