FROM python:3.7

WORKDIR /usr/src/web
ADD requirements.txt .
RUN pip install -r requirements.txt

CMD ["python", "main.py"]