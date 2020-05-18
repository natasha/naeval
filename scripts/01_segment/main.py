
from os.path import (
    expanduser,
    join as join_path
)
from inspect import isclass as is_class

from IPython.display import HTML
from tqdm.notebook import tqdm as log_progress

from naeval.log import log
from naeval.const import (
    CORPORA, SYNTAG, GICRYA, RNC,

    RE, DEEPPAVLOV, NLTK, SEGTOK, MOSES, RAZDEL,
    SPACY, TIMOFEEV, MYSTEM, SEGTOK, KOZIEV,

    DATASET, SENT, TOKEN, STATS, JL, GZ,
)
from naeval.io import (
    format_jl,
    parse_jl,

    load_lines,
    append_lines,

    load_gz_lines,
    dump_gz_lines,
)
from naeval.readme import patch_readme
from naeval.dataset import sample

from naeval.segment.partition import (
    Partition,
    parse_partitions,
    format_partitions,
    show_partition
)
from naeval.segment.datasets import (
    load_corpora,
    load_syntag,
    load_gicrya,
    load_rnc,

    parse_corpora_sents,
    parse_corpora_tokens,

    parse_syntag_sents,
    parse_syntag_tokens,

    parse_gicrya_sents,
    parse_gicrya_tokens,

    parse_rnc_sents,
    parse_rnc_tokens,
)
from naeval.segment.models import (
    Timing,

    re_sentenize,
    deeppavlov_sentenize,
    nltk_sentenize,
    segtok_sentenize,
    MosesSentenizer,
    razdel_sentenize,

    re_tokenize,
    nltk_tokenize,
    SpacyTokenizer,
    TimofeevTokenizer,
    MystemTokenizer,
    MosesTokenizer,
    segtok_tokenize,
    razdel_tokenize,
    KozievTokenizer,
)
from naeval.segment.score import score_partitions
from naeval.segment.report import (
    model_labels,
    report_table,
    format_report,
)


CORUS_DATA_DIR = expanduser('~/proj/corus-data')
CORUS_FILES = {
    CORPORA: ['annot.opcorpora.xml.byfile.zip'],
    SYNTAG: [
        'ud/syntag/ru_syntagrus-ud-dev.conllu',
        'ud/syntag/ru_syntagrus-ud-test.conllu',
        'ud/syntag/ru_syntagrus-ud-train.conllu'
    ],
    GICRYA: ['morphoru/gikrya_new_test.out', 'morphoru/gikrya_new_train.out'],
    RNC: ['morphoru/RNCgoldInUD_Morpho.conll']
}
DATA_DIR = expanduser('~/proj/naeval/data/segment')
README = expanduser('~/proj/naeval/README.md')
RAZDEL_README = expanduser('~/proj/razdel/README.md')

DATASETS = {
    CORPORA: load_corpora,
    SYNTAG: load_syntag,
    GICRYA: load_gicrya,
    RNC: load_rnc
}
PARSES = {
    SENT: {
        CORPORA: parse_corpora_sents,
        SYNTAG: parse_syntag_sents,
        GICRYA: parse_gicrya_sents,
        RNC: parse_rnc_sents
    },
    TOKEN: {
        CORPORA: parse_corpora_tokens,
        SYNTAG: parse_syntag_tokens,
        GICRYA: parse_gicrya_tokens,
        RNC: parse_rnc_tokens
    },
}
MODELS = {
    SENT: {
        RE: re_sentenize,
        SEGTOK: segtok_sentenize,
        MOSES: MosesSentenizer,
        NLTK: nltk_sentenize,
        DEEPPAVLOV: deeppavlov_sentenize,
        RAZDEL: razdel_sentenize,
    },
    TOKEN: {
        RE: re_tokenize,
        SPACY: SpacyTokenizer,
        NLTK: nltk_tokenize,
        MYSTEM: MystemTokenizer,
        MOSES: MosesTokenizer,
        SEGTOK: segtok_tokenize,
        TIMOFEEV: TimofeevTokenizer,
        KOZIEV: KozievTokenizer,
        RAZDEL: razdel_tokenize,
    }
}
