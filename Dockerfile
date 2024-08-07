FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . .
LABEL author="https://github.com/dnltv"
