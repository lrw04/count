FROM python:3.9.4-buster
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt && pip install gunicorn gevent
COPY . .
CMD ["gunicorn", "app:app", "-w", "4", "-k", "gevent", "-b", "0.0.0.0:80"]
