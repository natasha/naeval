
from os.path import (
    expanduser,
    join as join_path
)

from IPython.display import HTML
from tqdm.notebook import tqdm as log_progress

from naeval.const import (
    PERSONS, BSNLP,

    NATASHA,

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
from naeval.readme import patch_readme
from naeval.norm.datasets import load_persons, load_bsnlp
from naeval.norm.markup import (
    Markup,
    show_markup
)

CORUS_DATA_DIR = expanduser('~/proj/corus-data')
CORUS_FILES = {
    PERSONS: 'Persons-1000.zip',
    BSNLP: 'bsnlp'
}

DATASETS = [PERSONS, BSNLP]
DATA_DIR = expanduser('~/proj/naeval/data/norm')
NORM = 'norm'
README = expanduser('~/proj/naeval/README.md')
