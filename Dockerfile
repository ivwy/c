FROM python:3.10
WORKDIR /setup
COPY requirements.txt /setup/
RUN pip install -r requirements.txt
COPY . /setup
CMD python setup.py