FROM python:3.11-slim

RUN apt-get update && apt-get install -y nano

WORKDIR /app

COPY requerimientos.txt .

RUN pip install --no-cache-dir -r requerimientos.txt


COPY src ./src/
COPY tests /app/tests


CMD [ "python","src/semantic_search_students.py" ]
