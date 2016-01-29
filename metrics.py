from math import sqrt

def calc_Flesh_Kincaid_Grade_rus(n_syllabes, n_words, n_sent):
    """Метрика Flesh Kincaid Grade для русского языка"""

    n = 0.49 * (float(n_words) / n_sent) + 7.3 * (float(n_syllabes) / n_words) - 16.59
    return n

FLG_X_GRADE = 0.318
FLG_Y_GRADE = 14.2
FLG_Z_GRADE = 30.5


def calc_Flesh_Kincaid_Grade_rus_flex(n_syllabes, n_words, n_sent):
    """Метрика Flesh Kincaid Grade для русского языка с константными параметрами"""
    if n_words == 0 or n_sent == 0: return 0
    n = FLG_X_GRADE * (float(n_words) / n_sent) + FLG_Y_GRADE * (float(n_syllabes) / n_words) - FLG_Z_GRADE
    return n

CLI_X_GRADE = 0.055
CLI_Y_GRADE = 0.35
CLI_Z_GRADE = 20.33


def calc_Coleman_Liau_index(n_letters, n_words, n_sent):
    """ Метрика Coleman Liau для русского языка с константными параметрами """
    if n_words == 0: return 0
    n = CLI_X_GRADE * (n_letters * (100.0 / n_words)) - CLI_Y_GRADE * (n_sent * (100.0 / n_words)) - CLI_Z_GRADE
    return n

SMOG_X_GRADE = 1.1
SMOG_Y_GRADE = 64.6
SMOG_Z_GRADE = 0.05


def calc_SMOG_index(n_psyl, n_sent):
    """Метрика SMOG для русского языка с константными параментрами"""
    n = SMOG_X_GRADE * sqrt((float(SMOG_Y_GRADE) / n_sent) * n_psyl) + SMOG_Z_GRADE
    return n


DC_X_GRADE = 0.552
DC_Y_GRADE = 0.273

def calc_Dale_Chale_index(n_psyl, n_words, n_sent):
    """Метрика Dale Chale для русского языка с константным параметрами"""
    n = DC_X_GRADE * (100.0 * n_psyl / n_words) + DC_Y_GRADE * (float(n_words) / n_sent)
    return n

ARI_X_GRADE = 6.26
ARI_Y_GRADE = 0.2805
ARI_Z_GRADE = 31.04

def calc_ARI_index(n_letters, n_words, n_sent):
    """ Метрика Automated Readability Index (ARI) для русского языка с константными параметрами """
    if n_words == 0 or n_sent == 0: return 0
    n = ARI_X_GRADE * (float(n_letters) / n_words) + ARI_Y_GRADE * (float(n_words) / n_sent) - ARI_Z_GRADE
    return n



