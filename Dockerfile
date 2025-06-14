FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install grpcio grpcio-tools

#RUN python -m grpc_tools.protoc -I. --python_out=generated --grpc_python_out=generated contacts.proto

CMD ["tail", "-f", "/dev/null"]
