FROM python:3.7,7

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python3","api.py"]