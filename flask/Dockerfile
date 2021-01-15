FROM python:3.6

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install --upgrade pip

RUN pip install -r requirements.txt

COPY run.py /app
CMD python run.py
