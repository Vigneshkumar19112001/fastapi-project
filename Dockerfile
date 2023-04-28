FROM python:3.10.11

WORKDIR C:\Users\kumar g\application

COPY reqiurements.tct ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]