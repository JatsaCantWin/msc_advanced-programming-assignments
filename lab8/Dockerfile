FROM python:3.9-slim

WORKDIR /lab7

RUN pip install --no-cache-dir flask

COPY . .

EXPOSE 5000

CMD ["python", "service.py"]
