FROM ubuntu:18.04 AS build

RUN apt-get update && apt-get -y install gcc clang build-essential wget unzip

RUN wget https://github.com/ufal/udpipe/archive/v1.2.0.zip -O src.zip \
    && unzip src.zip \
    && mv udpipe-*/src . \
    && rm src.zip

RUN MODE=release make -C src server

RUN wget https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-2998/russian-syntagrus-ud-2.4-190531.udpipe -O model.udpipe

FROM ubuntu:18.04

COPY --from=build src/rest_server/udpipe_server .
COPY --from=build model.udpipe .

EXPOSE 8080
CMD ./udpipe_server 8080 model model ./model.udpipe desc --daemon && \
    tail -f udpipe_server.log

