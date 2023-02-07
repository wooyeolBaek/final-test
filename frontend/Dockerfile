FROM python:3.8.7-slim-buster

#LABEL maintainer="dwybaek7@gmail.com"

WORKDIR /app

COPY . /app

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

EXPOSE 8501

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]