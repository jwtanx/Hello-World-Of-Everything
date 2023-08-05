# Airflow

## Backfilling Airflow DAGs
1. Exec into the airflow scheduler container: `docker exec -it <scheduler_container_name> bash`
2. Backfill with the airflow command: `airflow dags backfill <dag_id> -s <starting_date> -e <ending_date>`

```bash
docker exec -it airflow-scheduler-1 bash
airflow dags backfill extract_ingest_pipeline -s 2023-04-20 -e 2023-07-20
```
NOTE: From the example given above, the date of the extracted data is from 2023-04-19 to 2023-07-19 (Not inclusive of the end data) command as the end date is not inclusive in the schedule). Always add one more day for your end date.