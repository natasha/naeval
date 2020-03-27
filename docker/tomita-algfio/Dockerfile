FROM python:3.5

RUN wget http://download.cdn.yandex.net/tomita/tomita-linux64.bz2 \
    && bzip2 -d tomita-linux64.bz2 \
    && chmod u+x tomita-linux64

COPY algfio algfio
COPY app.py .

ENV CONFIG_DIR algfio
ENV TOMITA_BIN tomita-linux64
CMD ["python", "app.py"]