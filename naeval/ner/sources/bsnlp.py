
from corus import load_bsnlp as load_bsnlp_

from naeval.const import BSNLP
from naeval.span import Span

from ..markup import Markup
from ..adapt import adapt_bsnlp


class BsnlpMarkup(Markup):
    label = BSNLP

    @property
    def adapted(self):
        return adapt_bsnlp(self)

    @classmethod
    def from_corus(self, record):
        return BsnlpMarkup(
            record.text,
            [Span(_.start, _.stop, _.type) for _ in record.spans]
        )


def load_bsnlp(dir):
    for record in load_bsnlp_(dir):
        yield BsnlpMarkup.from_corus(record)
