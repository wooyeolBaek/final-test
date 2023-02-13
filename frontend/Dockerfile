FROM gcr.io/heyi-front-test/heyi-front-base:latest

WORKDIR /frontend

COPY . /frontend

ENV PYTHONPATH=/frontend
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx libglib2.0-0 && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]
