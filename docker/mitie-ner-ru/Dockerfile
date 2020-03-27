FROM python:3.5

RUN wget http://lang.org.ua/static/downloads/ner_models/ru_model.dat.bz2 \
    && bzip2 -d ru_model.dat.bz2

RUN pip install --no-cache-dir git+https://github.com/mit-nlp/MITIE.git@v0.6

COPY app.py .
CMD ["python", "app.py"]