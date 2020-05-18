FROM python:3.6

RUN pip install --no-cache-dir spacy==2.1.4 pymorphy2==0.8

RUN wget https://github.com/buriy/spacy-ru/archive/v2.2.zip -O src.zip \
    && unzip src.zip \
    && mv spacy-ru-*/ru2 . \
    && rm -r src.zip spacy-ru-*

COPY app.py .
CMD ["python", "app.py", "tagger"]
