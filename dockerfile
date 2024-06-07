FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "--app", "src/web/run.py", "run", "--host=0.0.0.0", "--port=5000", "--debug"]
