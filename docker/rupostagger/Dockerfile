FROM python:3.6

RUN wget https://github.com/Koziev/rupostagger/archive/master.zip \
    && unzip master.zip \
    && mv rupostagger-* rupostagger \
    && rm master.zip

# important, otherwise
# No such file or directory: '/rupostagger/rupostagger/../tmp/rupostagger.config'"
RUN rm -r rupostagger/tmp

# manually install reqs from rupostagger/requirements
RUN pip install --no-cache-dir \
    pathlib \
    python-crfsuite \
    https://github.com/Koziev/rusyllab/archive/master.zip

# since one of them, ruword2tags does not install db file from lfs
RUN wget https://github.com/Koziev/ruword2tags/archive/master.zip \
    && unzip master.zip \
    && mv ruword2tags-* ruword2tags \
    && rm master.zip

RUN rm ruword2tags/ruword2tags/ruword2tags.db \
    && wget https://github.com/Koziev/ruword2tags/raw/master/ruword2tags/ruword2tags.db \
        -P ruword2tags/ruword2tags

RUN pip install --no-cache-dir -e ruword2tags
RUN pip install --no-cache-dir -e rupostagger

COPY app.py .
CMD ["python", "app.py"]