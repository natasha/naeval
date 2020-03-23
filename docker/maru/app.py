
import os
import sys
import json
from collections import OrderedDict
from datetime import datetime
from http import HTTPStatus
from http.server import (
    HTTPServer,
    BaseHTTPRequestHandler
)

import maru


HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', 8080))

TAGGER = os.getenv('TAGGER', 'rnn')
LEMMATIZER = os.getenv('LEMMATIZER', 'pymorphy')

ANALYZER = None


def log(format, *args):
    message = format % args
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(timestamp, message, file=sys.stderr, flush=True)


def process(words, analyzer):
    return analyzer.analyze(words)


def serialize_tag(tag):
    items = tag._asdict().items()
    for key, value in sorted(items):
        if value:
            yield key, value.value


def serialize(morphs):
    for record in morphs:
        yield OrderedDict([
            ('word', record.word),
            ('lemma', record.lemma),
            ('tag', OrderedDict(serialize_tag(record.tag)))
        ])


class HTTPHandler(BaseHTTPRequestHandler):
    error_message_format = '%(message)s'
    error_content_type = 'text/plain; charset=utf-8'

    def log_message(self, format, *args):
        # custom logging in do_POST
        pass

    def do_POST(self):
        if self.path != '/':
            self.send_error(
                HTTPStatus.NOT_FOUND,
                'Bad path: %r' % self.path
            )
            return

        length = self.headers.get('Content-Length')
        if not length or not length.isdigit():
            self.send_error(
                HTTPStatus.LENGTH_REQUIRED,
                'Bad Content-Length: %r' % length
            )
            return

        data = self.rfile.read(int(length))
        try:
            data = json.loads(data)
        except Exception as error:
            self.send_error(
                HTTPStatus.BAD_REQUEST,
                'Bad input data: "%s"' % error
            )
            return


        morphs = list(process(data, ANALYZER))
        log('Processed %d words', len(morphs))

        data = list(serialize(morphs))
        response = json.dumps(
            data,
            ensure_ascii=False,
            indent=2
        ).encode('utf8')

        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(response)


def main():
    try:
        log('Loading tagger: %s, lemmatizer: %s', TAGGER, LEMMATIZER)
        global ANALYZER
        ANALYZER = maru.get_analyzer(tagger=TAGGER, lemmatizer=LEMMATIZER)
    except Exception as error:
        log('Can not load analyzer: "%s"', error)
        return

    server = HTTPServer((HOST, PORT), HTTPHandler)
    try:
        log('Listening http://%s:%d', HOST, PORT)
        server.serve_forever()
    except KeyboardInterrupt:
        log('Quiting')
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
