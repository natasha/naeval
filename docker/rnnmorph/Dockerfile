FROM python:3.6

WORKDIR /

RUN pip install --no-cache-dir rnnmorph==0.4.0
COPY app.py .

CMD ["python", "app.py"]