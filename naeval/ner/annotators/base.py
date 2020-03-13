
from time import sleep

import requests

from naeval.const import LOCALHOST
from naeval.record import Record


class AnnotatorError(Exception):
    pass


def post(url, **kwargs):
    try:
        response = requests.post(url, **kwargs)
        response.raise_for_status()
        return response
    except requests.RequestException as error:
        message = str(error)
        raise AnnotatorError(message)


class Annotator(Record):
    __attributes__ = ['host', 'port']

    name = None
    image = None
    container_port = None

    payload = 'Путин наш президент'
    retries = 30
    delay = 2

    def __init__(self, host=LOCALHOST, port=8090):
        self.host = host
        self.port = port

    def __call__(self, text):
        raise NotImplementedError

    def map(self, texts):
        for text in texts:
            yield self(text)

    @property
    def ready(self):
        try:
            self(self.payload)
            return True
        except AnnotatorError:
            return False

    def wait(self, callback=None):
        for _ in range(self.retries):
            if self.ready:
                break
            else:
                if callback:
                    callback()
                sleep(self.delay)
        else:
            raise AnnotatorError('failed to start')


class ChunkAnnotator(Annotator):
    def map(self, texts):
        raise NotImplementedError

    def __call__(self, text):
        return next(self.map([text]))
