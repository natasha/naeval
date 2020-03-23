
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

from deeppavlov import build_model, configs


HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', 8080))

MODEL = None


def log(format, *args):
    message = format % args
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(timestamp, message, file=sys.stderr, flush=True)


def process(words, model):
    sents = [words]
    return model(sents)


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

        input = self.rfile.read(int(length))
        try:
            input = json.loads(input)
        except Exception as error:
            self.send_error(
                HTTPStatus.BAD_REQUEST,
                'Bad input data: "%s"' % error
            )
            return

        output = process(input, MODEL)
        log('Processed %d words', len(input))

        response = json.dumps(
            output,
            ensure_ascii=False,
            indent=2
        ).encode('utf8')

        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(response)


def main():
    try:
        log('Loading model')
        global MODEL
        MODEL = build_model(configs.morpho_tagger.UD2_0.morpho_ru_syntagrus_pymorphy)
    except Exception as error:
        log('Can not load model: "%s"', error)
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
