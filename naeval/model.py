
from time import sleep

import requests
from requests import ConnectionError, RequestException

from .const import LOCALHOST, PORT
from .record import Record
from .log import dot
from .docker import (
    docker_run,
    docker_rm
)


class ModelError(Exception):
    pass


def call(url, method, **kwargs):
    try:
        response = method(url, **kwargs)
        response.raise_for_status()
        return response
    except (ConnectionError, RequestException) as error:
        message = str(error)
        raise ModelError(message)


def get(url, **kwargs):
    return call(url, requests.get, **kwargs)


def post(url, **kwargs):
    return call(url, requests.post, **kwargs)


class ContainerModel(Record):
    __attributes__ = ['host', 'port']

    name = None
    image = None
    container_port = None

    payload = None
    retries = 1
    delay = 1

    def __init__(self, host=LOCALHOST, port=PORT):
        self.host = host
        self.port = port

    def __call__(self, item):
        raise NotImplementedError

    def map(self, items):
        for item in items:
            yield self(item)

    @property
    def ready(self):
        try:
            self(self.payload)
            return True
        except ModelError:
            return False

    def wait(self):
        for _ in range(self.retries):
            if self.ready:
                break
            else:
                dot()
                sleep(self.delay)
        else:
            raise ModelError('failed to start')

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


class ChunkMixin:
    def map(self, items):
        raise NotImplementedError

    def __call__(self, item):
        return next(self.map([item]))
