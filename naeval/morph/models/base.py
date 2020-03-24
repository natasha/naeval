
from naeval.model import (
    ContainerModel,
    ChunkMixin,
    post
)
from naeval.model import get  # noqa


class Model(ContainerModel):
    name = None
    image = None
    container_port = None
    url = 'http://{host}:{port}/'

    payload = ['Министр', 'общественного', 'порядка']
    retries = 30
    delay = 2

    def __call__(self, words):
        url = self.url.format(
            host=self.host,
            port=self.port
        )
        data = post(
            url,
            json=words
        ).json()
        return self.parse(data)


class ChunkModel(ChunkMixin, Model):
    pass
