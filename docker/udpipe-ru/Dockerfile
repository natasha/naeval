FROM ubuntu:18.04 AS build

RUN apt-get update
RUN apt-get -y install gcc clang build-essential unzip

ADD src.zip .
RUN unzip src.zip
RUN mv udpipe-*/src .

RUN MODE=release make -C src server

FROM ubuntu:18.04

COPY --from=build src/rest_server/udpipe_server .
ADD model.udpipe .

EXPOSE 8080
CMD ./udpipe_server 8080 model model ./model.udpipe desc --daemon && \
    tail -f udpipe_server.log

