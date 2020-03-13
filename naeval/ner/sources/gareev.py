
from corus import load_gareev as load_gareev_

from naeval.const import GAREEV
from naeval.span import Span

from ..markup import Markup
from ..adapt import adapt_gareev


class GareevMarkup(Markup):
    label = GAREEV

    @property
    def adapted(self):
        return adapt_gareev(self)

    @classmethod
    def from_corus(self, record):
        return GareevMarkup(
            record.text,
            [Span(*_) for _ in record.spans]
        )


def load_gareev(dir):
    for record in load_gareev_(dir):
        yield GareevMarkup.from_corus(record)
