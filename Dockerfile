FROM python:3.9-slim
WORKDIR /app
COPY . /app
COPY entrypoint /bin
ENTRYPOINT entrypoint