
from naeval.model import (
    ContainerModel,
    ChunkMixin,
)
from naeval.model import post, ModelError, ConnectionError  # noqa


class Model(ContainerModel):
    payload = 'Путин наш президент'
    retries = 30
    delay = 2


class ChunkModel(ChunkMixin, Model):
    pass
