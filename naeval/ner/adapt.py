
from naeval.const import PER, LOC, ORG
from naeval.span import (
    Span,
    convert_span_types,
    filter_empty_spans,
    filter_misaligned_spans,
    filter_overlapping_spans,
    select_type_spans,
    sort_spans,
    split_overlapping_spans,
    strip_spans,
    strip_spans_bounds
)
from naeval.tokenizer import tokenize

from .markup import Markup


QUOTES = '"\'”«„ʼ»“ʻ'
SPACES = ' \t'
DOT = '.'


def adapt_spans(spans, text, types):
    spans = select_type_spans(spans, types)
    spans = list(convert_span_types(spans, types))

    # ne5 typos is span.stop
    #   Magna Internationa -> Magna International
    #   Горсове -> Горсовет
    # tokenizer errors
    #   поезд Москва-Баку
    #   Yahoo!.
    tokens = list(tokenize(text))
    spans = filter_misaligned_spans(spans, tokens)
    return sort_spans(spans)


def adapt(markup, types):
    spans = list(adapt_spans(markup.spans, markup.text, types))
    return Markup(markup.text, spans)


#######
#
#   DEEPPAVLOV
#
###


DEEPPAVLOV_TYPES = {
    'PER': PER,
    'LOC': LOC,
    'ORG': ORG
}


def adapt_deeppavlov(markup):
    return adapt(markup, DEEPPAVLOV_TYPES)


#########
#
#   PULLENTI
#
#####


PULLENTI_TYPES = {
    'PERSON': PER,  # 11391
    'ORGANIZATION': ORG,  # 9723
    'GEO': LOC,  # 7234
    'STREET': LOC,  # 41
    'ADDRESS': LOC,  # 7

    # 'PERSONPROPERTY',  # 8350
    # 'MISSING',  # 43
}

BRACKETS = '()'
DASHES = '-'


def adapt_pullenti(markup):
    spans = list(split_overlapping_spans(markup.spans))
    spans = list(strip_spans(spans, markup.text, QUOTES + BRACKETS + DASHES + SPACES))
    spans = list(filter_empty_spans(spans))
    spans = list(adapt_spans(spans, markup.text, PULLENTI_TYPES))
    return Markup(markup.text, spans)


#########
#
#   TEXTERRA
#
###########


TEXTERRA_TYPES = {
    'PERSON': PER,  # 9119

    'GPE_COUNTRY': LOC,  # 3797
    'GPE_STATE_PROVINCE': LOC,  # 1341
    'GPE_CITY': LOC,  # 1329
    'GPE_OTHER': LOC,  # 59
    'LOCATION_LAKE_SEA_OCEAN': LOC,  # 12
    'LOCATION_OTHER': LOC,  # 10
    'LOCATION_REGION': LOC,  # 113
    'LOCATION_CONTINENT': LOC,  # 48
    'LOCATION_RIVER': LOC,  # 18

    'ORGANIZATION_POLITICAL': ORG,  # 2311
    'ORGANIZATION_CORPORATION': ORG,  # 1484
    'ORGANIZATION_OTHER': ORG,  # 689
    'ORGANIZATION_EDUCATIONAL': ORG,  # 213

    # For better precision do not treat
    # WORK_OF_ART, FACILITY as orgs, since
    # it not alway true (Черная кошка for example)

    # РБК daily, The Wall Street Journal
    # News of The World
    # 'WORK_OF_ART': ORG,  # 236
    # Русале, Лужников, Кремля, Домодедово
    # Пражском Граде  <- sometimes GEO
    # 'FACILITY': ORG,  # 200

    # 'NORP_RELIGION',  # 24 мусульманским, Бог, еврейских
    # 'NORP_NATIONALITY',  # 21 египтян, мордва
    # 'NORP_POLITICAL',  # 3 Лейбористы, социалистов
    # 'NORP_OTHER',  # 2 масон, афроамериканца

    # 'EVENT', # 134 Олимпиады в Сочи, День России, ВОВ
    # 'PRODUCT',  # 103 Google Maps, iOS, iPhone, истребителей F-16
    # 'SUBSTANCE',  # 41 никеля, алюминия, нефть
    # 'DISEASE',  # 22 ВИЭ, наркомании, СПИД, шизофренией
    # 'GAME',  # 15 футбольного, теннисист
    # 'LANGUAGE',  # 10 русскому языку, нидерландской, абхазского
    # 'ANIMAL',  # 5 Черепаха, Человек, заяц
    # 'PLANT',  # 1 табак
}


def adapt_texterra(markup):
    return adapt(markup, TEXTERRA_TYPES)


#######
#
#   TOMITA
#
#######


TOMITA_TYPES = {
    'PER': PER
}


def adapt_tomita(markup):
    return adapt(markup, TOMITA_TYPES)


#########
#
#    MITIE
#
######


MITIE_TYPES = {
    'PERS': PER,
    'ORG': ORG,
    'LOC': LOC,
}


def adapt_mitie(markup):
    # Чувашской Республики".
    # ----------------------
    # год Чарльза Дарвина»
    #     ----------------
    spans = list(strip_spans(markup.spans, markup.text, QUOTES + DOT + SPACES))
    spans = list(adapt_spans(spans, markup.text, MITIE_TYPES))
    return Markup(markup.text, spans)


##########
#
#   NATASHA
#
######


NATASHA_TYPES = {
    'Name': PER,  # 10039
    'Location': LOC,  # 9077
    'Organisation': ORG,  # 4158
}


def adapt_natasha(markup):
    spans = list(filter_overlapping_spans(markup.spans))
    spans = list(adapt_spans(spans, markup.text, NATASHA_TYPES))
    return Markup(markup.text, spans)


#########
#
#   FACTRU
#
######


# Org 2821
#     org_name 2333
#     org_descr 1700
#     loc_name 211
#     geo_adj 83
#     loc_descr 25
#     surname 17
#     job 7
#     name 5
#     nickname 2
# Person 2129
#     surname 1945
#     name 1336
#     nickname 65
#     patronymic 42
# LocOrg 1399
#     loc_name 1259
#     geo_adj 108
#     loc_descr 88
#     org_name 20
#     org_descr 9
# Location 1257
#     loc_name 1175
#     loc_descr 249
#     geo_adj 49
#     org_name 18
#     org_descr 15
#     surname 4
#     nickname 2
#     name 2
# Project 22 Вечерний Ургант, Пусть говорят, КВН, Пока все дома
# Facility 2 сайта Caramba TV


FACTRU_TYPES = {
    'Org': ORG,
    'Person': PER,
    'LocOrg': LOC,
    'Location': LOC
}


def select_spans(markup):
    for object in markup.objects:
        type = object.type
        if type == 'Person':
            yield Span(object.start, object.stop, object.type)
        elif type == 'Org':
            spans = [_ for _ in object.spans if _.type == 'org_name']
            for span in filter_overlapping_spans(spans):
                yield Span(span.start, span.stop, type)
        elif type in ('LocOrg', 'Location'):
            spans = [_ for _ in object.spans if _.type == 'loc_name']
            for span in filter_overlapping_spans(spans):
                yield Span(span.start, span.stop, type)


def adapt_factru(markup):
    spans = list(select_spans(markup))

    # мид Грузии
    # ORG-------
    #     LOC---
    spans = list(filter_overlapping_spans(spans))

    spans = list(adapt_spans(spans, markup.text, FACTRU_TYPES))
    return Markup(markup.text, spans)


#######
#
#   BSNLP
#
###


BSNLP_TYPES = {
    'PER': PER,
    'LOC': LOC,
    'ORG': ORG
}


def adapt_bsnlp(markup):
    return adapt(markup, BSNLP_TYPES)


##########
#
#   NE5
#
######


NE5_TYPES = {
    'GEOPOLIT': LOC,
    'LOC': LOC,
    'MEDIA': ORG,
    'ORG': ORG,
    'PER': PER,
}


def adapt_ne5(markup):
    # ne5 bug
    #   Бражский район Подмосковья
    #   --------------
    #            -----------------

    # компания "Союзкалий"
    #          -----------

    spans = list(filter_overlapping_spans(markup.spans))
    spans = strip_spans_bounds(spans, markup.text, QUOTES)
    spans = adapt_spans(spans, markup.text, NE5_TYPES)
    return Markup(markup.text, list(spans))


#########
#
#   GAREEV
#
#######


GAREEV_TYPES = {
    'PER': PER,
    'ORG': ORG,
}


def adapt_gareev(markup):
    # extra spaces + dots in spans

    # News Corp .
    # -----------

    # « Русал »
    # ---------

    spans = strip_spans(markup.spans, markup.text, DOT + SPACES)
    spans = strip_spans_bounds(spans, markup.text, QUOTES + SPACES)
    spans = adapt_spans(spans, markup.text, GAREEV_TYPES)
    return Markup(markup.text, list(spans))


######
#
#   WIKINER
#
#####


WIKINER_TYPES = {
    'PER': PER,
    'LOC': LOC,
    'ORG': ORG,
    # MISC drop
}


def adapt_wikiner(markup):
    # большевистской газете " Правда " .
    #                       ----------
    spans = strip_spans_bounds(markup.spans, markup.text, QUOTES + SPACES)
    spans = adapt_spans(spans, markup.text, WIKINER_TYPES)
    return Markup(markup.text, list(spans))
