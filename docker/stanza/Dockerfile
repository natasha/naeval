FROM pytorch/pytorch:1.4-cuda10.1-cudnn7-runtime

RUN pip install --no-cache-dir stanza==1.0.1
RUN python -c 'import stanza; stanza.download("ru")' \
    && rm ~/stanza_resources/ru/default.zip

COPY app.py .
CMD ["python", "app.py"]