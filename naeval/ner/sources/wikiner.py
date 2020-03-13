
from corus import load_wikiner as load_wikiner_

from naeval.const import WIKINER
from naeval.span import Span

from ..adapt import adapt_wikiner
from ..markup import Markup


class WikinerMarkup(Markup):
    label = WIKINER

    @property
    def adapted(self):
        return adapt_wikiner(self)

    @classmethod
    def from_corus(cls, record):
        return WikinerMarkup(
            record.text,
            [Span(*_) for _ in record.spans]
        )


def load_wikiner(path):
    for record in load_wikiner_(path):
        yield WikinerMarkup.from_corus(record)
