FROM python:3.9

MAINTAINER Bartosz Zurkowski

RUN GRPC_HEALTH_PROBE_VERSION=v0.3.6 && \
    wget -qO/bin/grpc_health_probe https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/${GRPC_HEALTH_PROBE_VERSION}/grpc_health_probe-linux-amd64 && \
    chmod +x /bin/grpc_health_probe

WORKDIR /app

ADD ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

RUN pip install .

ENV PYTHONUNBUFFERED=0

EXPOSE 7070

CMD [ "honcho", "--no-prefix", "start" ]
