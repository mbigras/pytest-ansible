FROM python:3.7.9

RUN apt-get update && apt-get install -y gosu

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY app.py entrypoint.sh ./

ENTRYPOINT ["/app/entrypoint.sh"]
