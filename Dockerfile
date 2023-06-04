FROM python:3.9

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . / .

EXPOSE 5000

CMD ["uvicorn", "app.main:app", "--port", "5000"]
