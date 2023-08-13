FROM python:3.11-slim as base

FROM base as runtime
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

FROM runtime as dev
COPY . /code/app

WORKDIR /code/app
#CMD ["uvicorn", "web_api:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8001", "-k", "uvicorn.workers.UvicornWorker", "web_api:app"]
