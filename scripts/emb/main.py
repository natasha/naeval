
from os.path import (
    expanduser,
    join as join_path
)

from IPython.display import HTML
from tqdm.notebook import tqdm as log_progress

from naeval.log import log
from naeval.const import (
    SIMLEX, HJ, RT, AE, AE2, LRWC,
    SOURCE, STATS, JL, JSON, GZ,
)
from naeval.record import (
    from_jsons,
    as_jsons
)
from naeval.io import (
    format_jl,
    parse_jl,
    format_json,
    parse_json,
    dump_text,
    load_text,
    dump_gz_lines,
    load_gz_lines
)

from naeval.emb.sources import (
    Sim,
    map_model,

    load_simlex,
    load_hj,
    load_rt,
    load_ae,
    load_ae2,
    load_lrwc,
)
from naeval.emb.models import (
    Stats,
    RusvectoresScheme,
    RusvectoresFasttextScheme,
    NavecScheme
)
from naeval.emb.score import (
    score_corr,
    score_prec
)
from naeval.emb.report import (
    report_table,
    format_report,
    format_github_report1,
    format_github_report2
)


CORUS_DATA_DIR = expanduser('~/proj/corus-data')
CORUS_FILES = {
    SIMLEX: 'simlex/ru_simlex965_tagged.tsv',
    HJ: 'russe/sem/hj.csv',
    RT: 'russe/sem/rt.csv',
    AE: ['russe/sem/ae-test.csv', 'russe/sem/ae-train.csv'],
    AE2: 'russe/sem/ae2.csv',
    LRWC: 'toloka/LRWC/lrwc-1.1-aggregated.tsv',
}
RUSVEC_DATA_DIR = expanduser('~/proj/rusvectores-data')
NAVEC_DATA_DIR = expanduser('~/proj/navec/data/models/navec/')
DATA_DIR = expanduser('~/proj/naeval/data/emb')

SOURCES = {
    SIMLEX: load_simlex,
    HJ: load_hj,
    RT: load_rt,
    AE: load_ae,
    AE2: load_ae2,
    LRWC: load_lrwc,
}
SCORES = {
    SIMLEX: score_corr,
    HJ: score_corr,
    RT: score_prec,
    AE: score_prec,
    AE2: score_prec,
    LRWC: score_prec,
}
SCHEMES = [
    RusvectoresScheme(
        'ruscorpora_upos_cbow_300_20_2019',
        join_path(RUSVEC_DATA_DIR, 'ruscorpora_upos_cbow_300_20_2019/model.bin')
    ),
    RusvectoresScheme(
        'ruwikiruscorpora_upos_skipgram_300_2_2019',
        join_path(
            RUSVEC_DATA_DIR,
            'ruwikiruscorpora_upos_skipgram_300_2_2019/model.bin'
        )
    ),
    RusvectoresScheme(
        'tayga_upos_skipgram_300_2_2019',
        join_path(RUSVEC_DATA_DIR, 'tayga_upos_skipgram_300_2_2019/model.bin')
    ),

    RusvectoresFasttextScheme(
        'tayga_none_fasttextcbow_300_10_2019',
        join_path(RUSVEC_DATA_DIR, 'tayga_none_fasttextcbow_300_10_2019/model.model')
    ),
    RusvectoresFasttextScheme(
        'araneum_none_fasttextcbow_300_5_2018',
        join_path(
            RUSVEC_DATA_DIR,
            'araneum_none_fasttextcbow_300_5_2018',
            'araneum_none_fasttextcbow_300_5_2018.model'
        )
    ),

    NavecScheme(
        'hudlit_12B_500K_300d_100q',
        join_path(NAVEC_DATA_DIR, 'navec_hudlit_v1_12B_500K_300d_100q.tar')
    ),
    NavecScheme(
        'news_1B_250K_300d_100q',
        join_path(NAVEC_DATA_DIR, 'navec_news_v1_1B_250K_300d_100q.tar')
    )
]
