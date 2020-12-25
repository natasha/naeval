FROM python:3.6

RUN pip install --no-cache-dir spacy==2.3.2 pymorphy2==0.8
RUN wget https://storage.yandexcloud.net/natasha-spacy/models/ru_core_news_md-2.3.0.tar.gz#rand=019312 \
    && pip install ru_core_news_md-2.3.0.tar.gz

COPY app.py .
CMD ["python", "app.py"]