FROM python:3.6

RUN pip install --no-cache-dir spacy==2.1.4 pymorphy2==0.8

ADD src.zip .
RUN unzip src.zip
RUN mv spacy-ru-*/ru2 .
RUN rm -r src.zip spacy-ru-*

COPY app.py .
CMD ["python", "app.py"]