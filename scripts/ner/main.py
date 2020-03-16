
from os.path import (
    expanduser,
    join as join_path
)
from random import seed, sample

from tqdm.notebook import tqdm as log_progress

from naeval.log import log
from naeval.const import (
    FACTRU, NE5,
    GAREEV, WIKINER, BSNLP,

    DEEPPAVLOV, DEEPPAVLOV_BERT,
    MITIE, NATASHA, PULLENTI,
    TEXTERRA, TOMITA,

    SOURCE, JL, GZ
)
from naeval.io import (
    format_jl,
    parse_jl,
    dump_gz_lines,
    load_gz_lines
)
from naeval.sent import iter_sents
from naeval.docker import docker_client
from naeval.ner.sources import (
    load_factru,
    load_bsnlp,
    load_ne5,
    load_gareev,
    load_wikiner
)
from naeval.ner.annotators import (
    TomitaAnnotator,
    PullentiAnnotator,
    MitieAnnotator,
    NatashaAnnotator,
    TexterraAnnotator,
    DeeppavlovAnnotator,
    DeeppavlovBERTAnnotator,
)
from naeval.ner.markup import (
    Markup,
    show_markup
)
from naeval.ner.score import score_markups
from naeval.ner.report import (
    report_table,
    format_report,
    format_github_report
)


CORUS_DATA_DIR = expanduser('~/proj/corus-data')
CORUS_FILES = {
    FACTRU: 'factRuEval-2016-master',
    BSNLP: 'bsnlp',
    NE5: 'Collection5',
    GAREEV: 'rus-ner-news-corpus.iob',
    WIKINER: 'aij-wikiner-ru-wp3.bz2',
}

SOURCES = {
    FACTRU: load_factru,
    GAREEV: load_gareev,
    NE5: load_ne5,
    BSNLP: load_bsnlp,
}
ANNS = {
    DEEPPAVLOV: DeeppavlovAnnotator,
    DEEPPAVLOV_BERT: DeeppavlovBERTAnnotator,
    PULLENTI: PullentiAnnotator,
    TEXTERRA: TexterraAnnotator,
    TOMITA: TomitaAnnotator,
    NATASHA: NatashaAnnotator,
    MITIE: MitieAnnotator,
}

DATA_DIR = expanduser('~/proj/naeval/data/ner')
