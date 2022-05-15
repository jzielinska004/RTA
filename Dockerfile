FROM python:3.8-slim

COPY ./requirements.txt /app/requirements.txt
COPY ./flask_server.py /app/flask_server.py
COPY ./model.pkl /app/model.pkl

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["flask_server.py"]