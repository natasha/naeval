# In 191 MaxRAMFraction is renamed to MaxRAMPercentage
FROM openjdk:8u181-jre

RUN wget https://at.ispras.ru/owncloud/index.php/s/Jkgrw6iIInwfKFv/download -O texterra-russian.zip \
    && unzip texterra-russian.zip \
    && rm texterra-russian.zip \
    && mv texterra-russian app

COPY texterra.properties.xml app
WORKDIR app

# If memory available to docker is 2Gb, for example, then max heap
# size is 500Mb, it is not enough to texterra, so set heap size equal
# to docker RAM
ENV JAVA_OPTS -XX:MaxRAMFraction=1

CMD ["bin/texterra", "-c", "texterra.properties.xml", "server", "start"]