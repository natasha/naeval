
import docker

from .record import Record


class DockerContainer(Record):
    __attributes__ = ['name', 'port']

    def __init__(self, name, port):
        self.name = name
        self.port = port


def docker_client():
    return docker.DockerClient()


def adapt_port(ports):
    # {'8080/tcp': [{'HostIp': '0.0.0.0', 'HostPort': '32768'}]}
    for container_port in ports:
        for item in ports[container_port]:
            return item['HostPort']


def adapt_container(record):
    port = adapt_port(record.ports)
    return DockerContainer(record.name, port)


def docker_list(client):
    for record in client.containers.list():
        yield adapt_container(record)


def docker_find(client, name):
    for record in docker_list(client):
        if record.name == name:
            return record


def docker_run(client, image, name, container_port, port):
    record = docker_find(client, name)
    if record:
        return record

    record = client.containers.run(
        image,
        name=name,
        ports={'%d/tcp' % container_port: port},
        detach=True
    )
    return adapt_container(record)


def docker_rm(client, name):
    for record in client.containers.list():
        if record.name == name:
            record.remove(force=True)
