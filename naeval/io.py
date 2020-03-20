
import gzip
import json
import xml.etree.ElementTree as ET


def load_text(path):
    with open(path) as file:
        return file.read()


def dump_text(text, path):
    with open(path, 'w') as file:
        file.write(text)


def load_lines(path):
    with open(path) as file:
        for line in file:
            yield line.rstrip('\n')


def dump_lines(lines, path):
    with open(path, 'w') as file:
        for line in lines:
            file.write(line + '\n')


def append_lines(lines, path):
    with open(path, 'a') as file:
        for line in lines:
            file.write(line + '\n')


def parse_xml(content):
    return ET.fromstring(content)


def load_gz_lines(path, encoding='utf8', gzip=gzip):
    with gzip.open(path) as file:
        for line in file:
            yield line.decode(encoding).rstrip()


def dump_gz_lines(lines, path):
    with gzip.open(path, 'wt') as file:
        for line in lines:
            file.write(line + '\n')


def format_jl(items):
    for item in items:
        yield json.dumps(item, ensure_ascii=False)


def parse_jl(lines):
    for line in lines:
        yield json.loads(line)


parse_json = json.loads
format_json = json.dumps
