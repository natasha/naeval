
import sys
from datetime import datetime


def dot():
    print('.', end='', file=sys.stderr, flush=True)


def log(format, *args):
    message = format % args
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(
        '[%s] %s' % (now, message),
        file=sys.stderr
    )
