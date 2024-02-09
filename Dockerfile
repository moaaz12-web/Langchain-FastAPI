FROM python:3.8.10-slim

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]