FROM python

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py app.py
COPY hoteles.py hoteles.py

CMD ["python3", "app.py"]

