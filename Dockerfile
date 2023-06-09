FROM python:3.10.11

WORKDIR /Users/kumar g/application

COPY reqiurements.txt ./

RUN pip install --no-cache-dir -r reqiurements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]