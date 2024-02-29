# Dockerfile

## Environment variable
```dockerfile
FROM debian:12-slim

ENV hello=123

CMD echo ${hello:-234}
```

## Changing user
```dockerfile
# docker build -f test_build.dockerfile -t airflow-testing --progress=plain --no-cache .
FROM harbor.company.com/abc/airflow_image_base:latest

RUN whoami
RUN which python
# RUN su airflow -c "pip install dummy_test"
# RUN su airflow -c "pip list"
RUN su airflow -c "whoami"
RUN whoami

RUN sudo -u airflow /bin/bash
RUN whoami
# RUN which python
# RUN pip list
```