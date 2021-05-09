FROM python:3.9-slim
RUN apk add --no-cache bash git curl
RUN mkdir /data
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT ["bash"]