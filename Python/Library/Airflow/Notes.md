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

## Render template as native object
Param as object and not string
```py
with DAG(
		dag_id='test',
		description='testing',
		default_args=DEFAULT_ARGS,
		params={
			'grocery_list': [
				'apple',
				'banana',
				'carrot'
			]
		},
		render_template_as_native_obj=True,
		schedule_interval='0 6 * * 4',
		start_date=datetime(2024, 8, 21, tzinfo=timezone.utc),
		max_active_runs=1,
		catchup=False,
		on_success_callback=Messager.on_success_callback,
		on_failure_callback=Messager.on_failure_callback,
		tags=['test']
) as dag:
	...
```
`render_template_as_native_obj` need to be set to `True` in order to render the template as native object or else the grocery_list will be rendered as string.

## Task using loops
https://stackoverflow.com/a/71154920
```py
from datetime import datetime

from airflow import DAG
from airflow.models.baseoperator import chain
from airflow.operators.python import PythonOperator

# Replace with your function logic
def hourly_job():
    return 'hourly'


# Replace with your function logic
def daily_job():
    return 'daily'


with DAG(dag_id='test', start_date=datetime(2022, 2, 16)) as dag:
    hours = ['01', '02', '03']
    op_list = [
        PythonOperator(task_id=f"task_hour_{hour}", python_callable=hourly_job, op_kwargs={"hour": hour})
        for hour in hours]
    chain(*op_list)
    t2 = PythonOperator(
        task_id="daily",
        python_callable=daily_job
    )

    op_list[-1] >> t2
```