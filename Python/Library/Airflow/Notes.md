# Airflow

## Backfilling Airflow DAGs
1. Exec into the airflow scheduler container: `docker exec -it <scheduler_container_name> bash`
2. Backfill with the airflow command: `airflow dags backfill <dag_id> -s <starting_date> -e <ending_date>`

```bash
docker exec -it airflow-scheduler-1 bash
airflow dags backfill extract_ingest_pipeline -s 2023-04-20 -e 2023-07-20
```
NOTE: From the example given above, the date of the extracted data is from 2023-04-19 to 2023-07-19 (Not inclusive of the end data) command as the end date is not inclusive in the schedule). Always add one more day for your end date.

## Dags
```py
"{{ dag_run.start_date }}" = 2024-06-11 03:35:48.798045+00:00
"{{ dag_run.execution_date }}" = 2024-06-10 07:00:00+00:00
"{{ dag_run.logical_date }}" = 2024-06-10 07:00:00+00:00
"{{ ds }}" = 2024-06-10
print(f"Run ID: {task_instance.run_id}")  # Run ID: scheduled__2023-08-09T00:00:00+00:00
print(f"Duration: {task_instance.duration}")  # Duration: 0.972019
print(f"DAG Run queued at: {dag_run.queued_at}")  # 2023-08-10 00:00:01+02:20
```