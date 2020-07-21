FROM python:3.7
ADD src /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "/app/flask_main.py"]
