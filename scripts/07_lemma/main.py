
from os.path import (
    expanduser,
    join as join_path
)

from IPython.display import HTML
from tqdm.notebook import tqdm as log_progress

from naeval.const import (
    NEWS, WIKI, FICTION, SOCIAL, POETRY,

    DATASET, JL, GZ
)
from naeval.io import (
    format_jl,
    parse_jl,

    load_gz_lines,
    dump_gz_lines,
)
from naeval.record import (
    as_jsons,
    from_jsons
)
from naeval.dataset import sample
from naeval.readme import patch_readme
from naeval.lemma.datasets import load_dataset
from naeval.lemma.markup import (
    Markup,
    show_markup
)

CORUS_DATA_DIR = expanduser('~/proj/corus-data/gramru')
CORUS_FILES = {
    NEWS: [
        'dev/GramEval2020-RuEval2017-Lenta-news-dev.conllu',
        'train/MorphoRuEval2017-Lenta-train.conllu',
    ],
    WIKI: [
        'dev/GramEval2020-GSD-wiki-dev.conllu',
        'train/GramEval2020-GSD-train.conllu'
    ],
    FICTION: [
        'dev/GramEval2020-SynTagRus-dev.conllu',
        'train/GramEval2020-SynTagRus-train-v2.conllu',
        'train/MorphoRuEval2017-JZ-gold.conllu'
    ],
    SOCIAL: [
        'dev/GramEval2020-RuEval2017-social-dev.conllu',
        'train/GramEval2020-Taiga-social-train.conllu',
        'train/MorphoRuEval2017-VK-gold.conllu'
    ],
    POETRY: [
        'dev/GramEval2020-Taiga-poetry-dev.conllu',
        'train/GramEval2020-Taiga-poetry-train.conllu'
    ],
}

DATASETS = [NEWS, WIKI, FICTION, SOCIAL, POETRY]

DATA_DIR = expanduser('~/proj/naeval/data/lemma')
LEMMA = 'lemma'
README = expanduser('~/proj/naeval/README.md')
