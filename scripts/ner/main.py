
from os.path import (
    expanduser,
    join as join_path
)

from IPython.display import HTML
from tqdm.notebook import tqdm as log_progress

from naeval.log import log
from naeval.const import (
    FACTRU, NE5,
    GAREEV, WIKINER, BSNLP,

    DEEPPAVLOV, DEEPPAVLOV_BERT,
    MITIE, NATASHA, PULLENTI,
    TEXTERRA, TOMITA,

    SOURCE, JL, GZ,

    GPU, KB, MB, GB
)
from naeval.record import (
    from_jsons,
    as_jsons
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
from naeval.ner.models import (
    TomitaModel,
    PullentiModel,
    MitieModel,
    NatashaModel,
    TexterraModel,
    DeeppavlovModel,
    DeeppavlovBERTModel,
)
from naeval.ner.markup import (
    Markup,
    show_markup
)
from naeval.ner.score import score_markups
from naeval.ner.report import (
    scores_report_table,
    format_scores_report,
    format_github_scores_report,

    Bench,
    format_bench_report
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
MODELS = {
    DEEPPAVLOV: DeeppavlovModel,
    DEEPPAVLOV_BERT: DeeppavlovBERTModel,
    PULLENTI: PullentiModel,
    TEXTERRA: TexterraModel,
    TOMITA: TomitaModel,
    NATASHA: NatashaModel,
    MITIE: MitieModel,
}

DATA_DIR = expanduser('~/proj/naeval/data/ner')
