
from time import sleep

import requests
from requests import ConnectionError, RequestException

from naeval.const import LOCALHOST, PORT
from naeval.record import Record
from naeval.log import dot
from naeval.docker import (
    docker_run,
    docker_rm
)


class AnnotatorError(Exception):
    pass


def post(url, **kwargs):
    try:
        response = requests.post(url, **kwargs)
        response.raise_for_status()
        return response
    except (ConnectionError, RequestException) as error:
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

    def __init__(self, host=LOCALHOST, port=PORT):
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

    def wait(self):
        for _ in range(self.retries):
            if self.ready:
                break
            else:
                dot()
                sleep(self.delay)
        else:
            raise AnnotatorError('failed to start')

    def start(self, client):
        docker_run(
            client,
            self.image,
            self.name,
            self.container_port,
            self.port
        )

    def stop(self, client):
        docker_rm(client, self.name)


class ChunkAnnotator(Annotator):
    def map(self, texts):
        raise NotImplementedError

    def __call__(self, text):
        return next(self.map([text]))
