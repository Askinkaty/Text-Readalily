# -*- coding: utf-8 -*-
from process_gram import process_grammar
import codecs

first_pp = ['мы', 'я', 'наш', 'мой']
second_pp = ['ты', 'вы', 'ваш', 'твой']
third_pp = ['он', 'она', 'они', 'оно', 'их', 'ee', 'его', 'ихний', 'ихним', 'ихнем']
indef_pron = ['некто', 'некого', 'некому', 'некем', 'нечто', 'нечего', 'нечему', 'нечем', 'некоторый', 'некий', 'любой',
              'никто', 'ничто', 'никакой', 'нисколько', 'нигде', 'негде', 'некуда', 'никуда', 'неоткуда', 'ниоткуда',
              'некогда', 'никогда', 'никак', 'незачем', 'незачем']
place_adverbs = ['близко', 'ближе', 'вблизи', 'вверх', 'вверху', 'ввысь', 'вглубь', 'вдали', 'вдаль', 'везде', 'взад',
                 'влево', 'вне', 'вниз', 'внизу', 'внутри', 'внутрь', 'вовне', 'вовнутрь', 'вокруг', 'вперед',
                 'впереди', 'вправо', 'всюду', 'высоко', 'выше', 'глубоко', 'глубже', 'далеко', 'дальше', 'донизу',
                 'дома', 'здесь', 'издалека', 'издалече', 'издали', 'изнутри', 'кверху', 'книзу', 'кругом', 'левее',
                 'наверх', 'наверху', 'наискосок', 'налево', 'направо', 'напротив', 'наружно', 'наружу', 'невысоко',
                 'неглубоко', 'недалеко', 'неподалеку', 'низко', 'ниже', 'одаль', 'около', 'окрест', 'особняком',
                 'отдельно', 'откуда', 'отсюда', 'поближе', 'поверх', 'повсеместно', 'повсюду', 'повыше', 'поглубже',
                 'подальше', 'позади', 'пониже', 'понизу', 'посередке', 'посередине', 'посреди', 'посредине', 'поодаль',
                 'правее', 'рядом', 'сбоку', 'сверху', 'свыше', 'сзади', 'слева', 'снизу', 'снаружи', 'спереди',
                 'справа', 'стороной', 'супротив']
time_adverbs = ['бесконечно', 'беспрерывно', 'ввек', 'весной', 'вечно', 'вмиг', 'вначале', 'вовек', 'вовремя', 'впору',
                'впоследствии',
                'впредь', 'враз', 'временно', 'всечасно', 'вскоре', 'встарь', 'вчера', 'вчерась', 'давеча', 'давно',
                'давненько', 'денно', 'длительно', 'днесь', 'доколе', 'долго', 'дольше', 'доныне',
                'досветла', 'доселе', 'досрочно', 'дотемна', 'доутра', 'единовременно', 'ежеквартально', 'ежеминутно',
                'еженощно', 'ежесекундно', 'ежечасно', 'еще', 'заблаговременно', 'завсегда', 'завтра', 'задолго',
                'загодя', 'заранее', 'зараз', 'засим', 'затем', 'зимой', 'извечно', 'издревле', 'изначально', 'иногда',
                'исконно', 'испокон', 'исстари', 'круглосуточно', 'кряду', 'летом', 'мимолетно', 'навек', 'навеки',
                'навсегда', 'надолго', 'назавтра', 'накануне', 'наконец', 'намедни', 'наперед', 'напоследок',
                'напролет', 'насовсем', 'наутро', 'недавно', 'недолго', 'незадолго', 'незамедлительно', 'ненадолго',
                'нескоро', 'неоднократно', 'нонче', 'непрерывно', 'непродолжительно', 'нощно', 'ныне', 'нынче',
                'однажды', 'одновременно', 'осенью', 'отколе', 'отныне', 'отродясь', 'первоначально', 'позавчера',
                'позднее', 'поздно', 'поздновато', 'позже', 'подолгу', 'подряд', 'пожизненно', 'пока', 'покамест',
                'поныне', 'поначалу', 'попозже', 'пораньше', 'после', 'послезавтра',
                'поспешно', 'поскорее', 'постоянно', 'поутру', 'прежде', 'преждевременно', 'присно',
                'продолжительно', 'редко', 'реже', 'ранее', 'рано', 'рановато', 'раньше', 'редко', 'своевременно',
                'сегодня', 'скорее', 'скорей', 'скоро', 'смолоду', 'сначала', 'сперва', 'сразу', 'срочно', 'сроду',
                'теперича', 'часто', 'уже', 'ужо']
interrogative_pronoun = ['кто', 'что', 'какой', 'каков', 'чей', 'который', 'почему', 'зачем', 'где', 'куда', 'откуда',
                         'отчего']


def is_have_grammar(e):
    # try:
    return e[1] != ''
    # except KeyError as ke:
    #     print("Key error:" + str(e))
    #     raise ke


# 1
# test that the current word is a first person pronoun
def first_person_pronoun(t):
    fpp1 = 0
    for el in t:
        if el[2] in first_pp:
            fpp1 += 1
    return fpp1


# 2
# test that the current word is a second person pronoun
def second_person_pronoun(t):
    spp2 = 0
    for el in t:
        if el[2] in second_pp:
            spp2 += 1
    return spp2


# 3
# test that the current word is a third person pronoun
def third_person_pronoun(t):
    tpp3 = 0
    for el in t:
        if el[2] in third_pp:
            tpp3 += 1
    return tpp3


# 4
# test that the current word is a pronoun
def is_pronoun(t):
    pron = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'P':
                pron += 1
        else:
            continue
    return pron


# 5
# test that the current word is a finite verb
def is_finite_verb(t):
    finite = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'V' and d_el.get('vform') == 'i':
                finite += 1
        else:
            continue
    return finite


# 6
# test that the current word is an adjective or a participle
# may be we should leave only test for adjectives and add a test that they are modifiers and not parts of predicates
def is_modifier(t):
    mod = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'A' or (d_el.get('pos') == 'V' and d_el.get('vform') == 'p'):
                mod += 1
        else:
            continue
    return mod


# 7
# test that the current word has a past tense form
def past_tense(t):
    past = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'V' and d_el.get('tense') == 's':
                past += 1
        else:
            continue
    return past


# 8
# test that the current word has a perfect aspect form
def perf_aspect(t):
    perf = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'V' and d_el.get('aspect') == 'p':
                perf += 1
        else:
            continue
    return perf


# 9
# test that the current word has a present tense form
def present_tense(t):
    pres = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'V' and d_el.get('tense') == 'p':
                pres += 1
        else:
            continue
    return pres


# 10
# test that the current word is an adverb
def total_adverb(t):
    total_adv = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'R':
                total_adv += 1
        else:
            continue
    return total_adv


# nouns
# 11
# 12
# test that the current word a verbal noun (отглагольное сущ.) or not verbal noun
def is_nominalization(t):
    nomz = 0
    nouns = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'N':
                with codecs.open('dictionaries/final_lemmas_nominalizations.txt', mode='r', encoding='utf-8') as f:
                    read_lines = set([s.strip() for s in f.readlines()])
                    if el[2].lower() in read_lines:
                        nomz += 1
                    else:
                        nouns += 1
        else:
            continue
    return nomz, nouns


# 13
# test that the current word has a genitive case form
def is_genitive(t):
    gen = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if (d_el.get('pos') == 'N' or d_el.get('pos') == 'P' or d_el.get('pos') == 'A') and d_el.get('case') == 'g':
                gen += 1
        else:
            continue
    return gen


# 14
# test that the current word has a neuter gender form
def is_neuter(t):
    neuter = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if ((d_el.get('pos') == 'N' or d_el.get('pos') == 'P' or d_el.get('pos') == 'A')
                and d_el.get('gender') == 'n'):
                neuter += 1
        else:
            continue
    return neuter


# 15
# test that the current word has a passive form
def is_passive(t):
    passive = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'V' and 'p' == d_el.get('voice'):
                passive += 1
        else:
            continue
    return passive


# 16
# test that the current verb is an infinitive
def infinitives(t):
    infin = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'V' and d_el.get('vform') == 'n':
                infin += 1
        else:
            continue
    return infin


# 17
# test that the current word is a speech verb
def speech_verb(t):
    sp_verb = 0
    with codecs.open(r'dictionaries/all_lemmas_verb_speech.txt', mode='r', encoding='utf-8') as f:
        read_lines = set([s.strip() for s in f.readlines()])
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'V':
                if el[2].lower() in read_lines:
                    sp_verb += 1
        else:
            continue
    return sp_verb


# 18
# test that the current word is a mental verb
def mental_verb(t):
    mntl_verb = 0
    with codecs.open(r'dictionaries/all_lemmas_verb_mental.txt', mode='r', encoding='utf-8') as f:
        read_lines = set([s.strip() for s in f.readlines()])
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'V':
                if el[2].lower() in read_lines:
                    mntl_verb += 1
        else:
            continue
    return mntl_verb


# 19
# test that the current sentence includes that-complement clause
def that_complement(t):
    that_compl = 0
    l = len(t)
    for i, el in enumerate(t):
        if is_have_grammar(el):
            if t[l - 1][0] != '?':
                d_el = process_grammar(el)
                d_next_el = {}
                if i + 1 < len(t):
                    next_el = t[i + 1]
                    d_next_el = process_grammar(next_el)
                    d_next_el = d_next_el if d_next_el is not None else {}
                    # test that current word is verb or short-form adjective and the next word is not a verb or
                    # short-form adjective because of sentences like 'Я был счастлив, что она пришла'.

                    if d_el.get('pos') == 'V' or (d_el.get('pos') == 'A' and d_el.get('definiteness') == 's'):
                        if is_have_grammar(next_el):
                            if (d_next_el.get('pos') != 'V' and
                                    (d_next_el.get('pos') != 'A' or d_next_el.get('definiteness') != 's')):
                                for j in range(4):
                                    # test that there's no pronouns like 'то, это, такой' between the current word and comma
                                    # because of sentences like 'Я не предвидел того, что вы приедете',
                                    #  which has relative meaning.
                                    # test that conjunction like 'что', 'чтобы' directly follow after comma
                                    if (i + j + 1 < len(t) and
                                                t[i + j][2] not in ['весь', 'все', 'такой', 'то', 'это', 'тот',
                                                                    'этот'] and
                                                t[i + j + 1][0] == ',' and i + j + 2 < len(t) and
                                                t[i + j + 2][2] in ['что', 'чтобы']):
                                        if i + j + 3 < len(t):
                                            # test that if the conjunction is 'чтобы', there's no infinitive verb after it
                                            # to check that it's not an infinitive clause
                                            if t[i + j + 2][2] == 'чтобы':
                                                if is_have_grammar(t[i + j + 3]):
                                                    d_is_inf_el = process_grammar(t[i + j + 3])
                                                    if d_is_inf_el.get('pos') == 'V' and d_is_inf_el.get(
                                                            'vform') == 'n':
                                                        continue
                                                    else:
                                                        that_compl += 1
                                            else:
                                                that_compl += 1
                        else:
                            continue
        else:
            continue
    return that_compl


# 20
# test that the current sentence includes wh-relative clause (относительное придаточное)
def wh_relatives(t):
    wh_relative = 0
    l = len(t)
    # test that sentence is not interrogative
    if t[l - 1][0] != '?':
        for i, el in enumerate(t):
            # test that pronoun is in the left periphery of the sentence and preceded by comma
            if el[2] in ['какой', 'чей', 'который', 'почему', 'зачем', 'где', 'куда', 'откуда', 'отчего']:
                d_prev_el = {}
                if i - 1 > 0:
                    prev_el = t[i - 1]
                    if prev_el[0] == ',':
                        wh_relative += 1
            # test that there's the example of relative clause structure like "Это был тот, кого я не боюсь".
            if el[2] in ['кто']:
                if i - 1 > 0:
                    prev_el = t[i - 1]
                    if prev_el[0] == ',':
                        if i - 2 > 0 and t[i - 2][2] in ['тот', 'то', 'все', 'весь', 'такой']:
                            wh_relative += 1
            else:
                continue
    return wh_relative


# 21
# test that the current word is preposition
# (we count all prepositional phrases in the sentence by counting prepositions)
def total_PP(t):
    prep_phrase = 0
    with codecs.open(r'dictionaries/all_lemmas_prepositions.txt', mode='r', encoding='utf-8') as f:
        prepositions = set([s.strip() for s in f.readlines()])
    for i, el in enumerate(t):
        if el[2] in prepositions:
            prep_phrase += 1
        else:
            if is_have_grammar(el):
                d_el = process_grammar(el)
                if d_el.get('pos') == 'S' and el[0] != '.':
                    prep_phrase += 1
            else:
                continue
    return prep_phrase


# 22
# function for counting mean word length
# it is possibly better to count median word length
def word_length(t):
    words = 0
    letters = 0
    for el in t:
        if el[0] not in ['.', ',', '!', '?', ':', ';', '"', '-', '—', '–']:
            words += 1
            for let in el[0]:
                letters += 1
        else:
            continue
    return letters, words


# 23
# function for counting all syllables in the sentence
def syllables(t):
    syll = 0
    complex_w = 0
    for el in t:
        for ch in el[0]:
            if ch in ['а', 'о', 'у', 'и', 'ы', 'е', 'ё', 'я', 'э', 'ю']:
                syll += 1
        if syll > 4:
            complex_w += 1
    return syll, complex_w


# 24
# interval between punctuation marks
def text_span(t):
    result = 0
    sent_span = 0
    p = 0
    list_of_spans = []

    for i, el in enumerate(t):
        if el[0] in ['.', ',', '!', '?', ':', ';', '"', '-', '—', '–']:
            sent_span = i - p
            list_of_spans.append(sent_span)
            p = i

    if len(list_of_spans) == 0:
        result = 0
    else:
        result = sum(list_of_spans) / len(list_of_spans)
    return result


# 25
# function for counting mean sentence length
def sentence_length(t):
    sent_words = 0
    for el in t:
        if el[0] not in ['.', ',', '!', '?', ':', ';', '"', '-', '—', '–'] and el[1] != 'SENT':
            sent_words += 1
    return sent_words


# 26
# function for counting relation between lemmas and tokens (how many original words does the text include?)
def type_token_ratio(t):
    types = set()
    tokens = 0
    for el in t:
        if el[0] not in ['.', ',', '!', '?', ':', ';', '"', '-', '—', '–', '@', '#', '"', '$', '%', '*', '+', ')', '(',
                         '[', ']', '{', '}', '&']:
            types.add(el[2])
            tokens += 1
        else:
            continue
    return types, tokens


# 27
# test that the current word is a verbal adverb (деепричастие)
def is_verbal_adverb(t):
    gerund = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'V' and d_el.get('vform') == 'g':
                gerund += 1
        else:
            continue
    return gerund


# 28
# test that the sentence includes passive participles not in predicate position
def passive_participial_clauses(t):
    pas_part_clauses = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            flag_predicate = False
            d_el = process_grammar(el)
            # test that current word is past participle
            if d_el.get('pos') == 'V' and d_el.get('vform') == 'p' and d_el.get('voice') == 'p':
                d_prev_el = {}
                d_prev_prev_el = {}
                if i > 0:
                    prev_el = t[i - 1]
                    d_prev_el = process_grammar(prev_el)
                    d_prev_el = d_prev_el if d_prev_el is not None else {}
                    # test that the word is not a part of predicate like 'быть уставшим', 'становиться раздраженным'
                    if d_prev_el.get('pos') == 'V' and prev_el[2].lower() in ['быть', 'делаться', 'сделаться',
                                                                              'казаться',
                                                                              'называться', 'становиться', 'являться']:
                        flag_predicate = True
                if i - 1 > 0:
                    prev_el = t[i - 1]
                    prev_prev_el = t[i - 2]
                    d_prev_el = process_grammar(prev_el)
                    d_prev_el = d_prev_el if d_prev_el is not None else {}
                    d_prev_prev_el = process_grammar(prev_prev_el)
                    d_prev_prev_el = d_prev_prev_el if d_prev_prev_el is not None else {}
                    # test that the word is not a part of predicate separated by adverb or patricles from the list
                    if d_prev_prev_el.get('pos') == 'V' and prev_prev_el[2].lower() in ['быть', 'делаться', 'сделаться',
                                                                                        'казаться',
                                                                                        'называться', 'становиться',
                                                                                        'являться']:
                        if d_prev_el.get('pos') == 'R' or prev_el[0].lower() in ['ли', 'бы', 'не']:
                            flag_predicate = True

                if not flag_predicate:
                    pas_part_clauses += 1
        else:
            continue
    return pas_part_clauses


# 29
# test that the sentence includes active participles not in predicate position
def active_participial_clauses(t):
    act_part_clauses = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            flag_predicate = False
            d_el = process_grammar(el)
            # test that current word is active/medial participle
            if d_el.get('pos') == 'V' and d_el.get('vform') == 'p' and d_el.get('voice') != 'p':
                d_prev_el = {}
                d_prev_prev_el = {}
                if i > 0:
                    prev_el = t[i - 1]
                    d_prev_el = process_grammar(prev_el)
                    d_prev_el = d_prev_el if d_prev_el is not None else {}
                    # test that the word is not a part of predicate like 'быть потрясающим'
                    if d_prev_el.get('pos') == 'V' and prev_el[2].lower() in ['быть', 'делаться', 'сделаться',
                                                                              'казаться',
                                                                              'называться', 'становиться', 'являться']:
                        flag_predicate = True
                if i - 1 > 0:
                    prev_el = t[i - 1]
                    prev_prev_el = t[i - 2]
                    d_prev_el = process_grammar(prev_el)
                    d_prev_el = d_prev_el if d_prev_el is not None else {}
                    d_prev_prev_el = process_grammar(prev_prev_el)
                    d_prev_prev_el = d_prev_prev_el if d_prev_prev_el is not None else {}
                    # test that the word is not a part of predicate separated by adverb or patricles from the list
                    if d_prev_prev_el.get('pos') == 'V' and prev_prev_el[2].lower() in ['быть', 'делаться', 'сделаться',
                                                                                        'казаться',
                                                                                        'называться', 'становиться',
                                                                                        'являться']:
                        if d_prev_el.get('pos') == 'R' or prev_el[0].lower() in ['ли', 'бы', 'не']:
                            flag_predicate = True

                if not flag_predicate:
                    act_part_clauses += 1
        else:
            continue
    return act_part_clauses


# 30
# test that the current word has an imperative mood form
def imperative_mood(t):
    imp_mood = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            d_prev = {}
            d_next_el = {}
            # test that catch constructions like "давайте пишите" to assign only one mark of imperative mood
            if d_el.get('pos') == 'V' and d_el.get('vform') == 'm':
                if el[0].lower() == 'давайте' or el[0].lower() == 'давай':
                    pass
                else:
                    imp_mood += 1
            # test that catch only "давай/те" without any verb after it
            if el[0].lower() == 'давайте' or el[0].lower() == 'давай':
                if i + 1 < len(t):
                    next_el = t[i + 1]
                    if is_have_grammar(next_el):
                        d_next_el = process_grammar(next_el)
                        d_next_el = d_next_el if d_next_el is not None else {}
                        if d_next_el.get('pos') != 'V':
                            imp_mood += 1
                        elif d_next_el.get('vform') != 'm':
                            imp_mood += 1
                        else:
                            continue
            if i > 0:
                prev_el = t[i - 1]
                if d_el.get('pos') == 'V' and d_el.get('vform') == 'i' and d_el.get('person') == '3':
                    if prev_el[0].lower() in ['да', 'пусть', 'пускай']:
                        imp_mood += 1
        else:
            continue
    return imp_mood


# 31
# test that the current word is an adjective in predicative position
def predicative_adjectives(t):
    pred_adj = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'A' and d_el.get('definiteness') == 's':
                pred_adj += 1
            if d_el.get('pos') == 'A' and d_el.get('definiteness') == 'f':
                d_prev_el = {}
                if i > 0:
                    prev_el = t[i - 1]
                    if is_have_grammar(prev_el):
                        d_prev_el = process_grammar(prev_el)
                        d_prev_el = d_prev_el if d_prev_el is not None else {}
                        if d_prev_el.get('pos') == 'V' and prev_el[2] in ['быть', 'делаться', 'сделаться', 'казаться',
                                                                          'называться', 'становиться', 'являться']:
                            pred_adj += 1
            else:
                continue
        else:
            continue
    return pred_adj


# 32
# test that the current word is an adjective in attributive position
def attributive_adjective(t):
    attr_adj = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            flag_predicate = False
            if d_el.get('pos') == 'A' and d_el.get('definiteness') == 'f':
                d_prev_el = {}
                if i > 0:
                    prev_el = t[i - 1]
                    if is_have_grammar(prev_el):
                        d_prev_el = process_grammar(prev_el)
                        d_prev_el = d_prev_el if d_prev_el is not None else {}
                        if d_prev_el.get('pos') == 'V' and prev_el[2] in ['быть', 'делаться', 'сделаться', 'казаться',
                                                                          'называться', 'становиться', 'являться']:
                            flag_predicate = True
                if not flag_predicate:
                    attr_adj += 1
                else:
                    continue
        else:
            continue
    return attr_adj


# 33
# test that the sentence includes causative subordinate clause
def causative_subordinate(t):
    causative_sub = 0
    for i, el in enumerate(t):
        if el[0] in ['поскольку', 'ибо']:
            causative_sub += 1
        else:
            if i > 0:
                prev_el = t[i - 1]
                # test that conjunction is 'так как'
                if prev_el[0] == 'так' and el[0] == 'как':
                    causative_sub += 1
            if i + 1 < len(t):
                next_el = t[i + 1]
                # test that conjunction is 'затем что', 'потому что', 'оттого что'
                if el[0] in ['затем', 'потому', 'оттого'] and next_el[0] == 'что':
                    causative_sub += 1
            if i + 2 < len(t):
                next_el = t[i + 1]
                next_next_el = t[i + 2]
                # test that conjunction is 'затем что', 'потому что', 'оттого что' separated by comma ('потому, что')
                if el[0] in ['затем', 'потому', 'оттого'] and next_el[0] == ',' and next_next_el[0] == 'что':
                    causative_sub += 1
                # test that conjunction is 'ввиду того что', 'вследствие того что', 'благодаря тому что'
                if el[0] in ['ввиду', 'вследствие', 'благодаря'] and next_el[2] == 'то' and next_next_el[0] == 'что':
                    causative_sub += 1
            if i + 3 < len(t):
                next_el = t[i + 1]
                next_next_el = t[i + 2]
                next_next_next_el = t[i + 3]
                # test that conjunction is 'ввиду того, что', 'вследствие того, что', 'благодаря тому, что'
                if (el[0] in ['ввиду', 'вследствие', 'благодаря'] and next_el[2] == 'то' and
                            next_next_el[0] == ',' and next_next_next_el[0] == 'что'):
                    causative_sub += 1
            if i + 2 < len(t) and i > 0:
                prev_el = t[i - 1]
                next_el = t[i + 1]
                next_next_el = t[i + 2]
                # test that conjunction is 'в силу того что'
                if el[0] == 'силу' and prev_el[0] == 'в' and next_el[2] == 'то' and next_next_el[0] == 'что':
                    causative_sub += 1
            if i + 3 < len(t) and i > 0:
                prev_el = t[i - 1]
                next_el = t[i + 1]
                next_next_el = t[i + 2]
                next_next_next_el = t[i + 3]
                # test that conjunction is 'в силу того, что'
                if (el[0] == 'силу' and prev_el[0] == 'в' and next_el[2] == 'то' and next_next_el[0] == ',' and
                            next_next_next_el[0] == 'что'):
                    causative_sub += 1
                # test that conjunction is 'в связи с тем что'
                if (el[0] == 'связи' and prev_el[0] == 'в' and next_el[0] == 'с' and next_next_el[2] == 'то' and
                            next_next_next_el[0] == 'что'):
                    causative_sub += 1
            if i + 4 < len(t) and i > 0:
                prev_el = t[i - 1]
                next_el = t[i + 1]
                next_next_el = t[i + 2]
                next_next_next_el = t[i + 3]
                next_next_next_next_el = t[i + 4]
                # test that conjunction is 'в связи с тем, что'
                if (el[0] == 'связи' and prev_el[0] == 'в' and next_el[0] == 'с' and next_next_el[2] == 'то' and
                    next_next_next_el[0] == ',' and next_next_next_next_el[0] == 'что'):
                    causative_sub += 1
            else:
                continue
    return causative_sub


# 34
# test that the sentence includes concessive subordinate clause
def concessive_subordinate(t):
    concessive_sub = 0
    for i, el in enumerate(t):
        d_next_el = {}
        if el[0] == 'хоть':
            concessive_sub += 1
        if i + 1 < len(t):
            next_el = t[i + 1]
            if el[0] == 'даром' and next_el[0] == 'что':
                concessive_sub += 1
            if el[0] in ['несмотря', 'невзирая'] and next_el[0] == 'на':
                concessive_sub += 1
            if el[0] in ['только', 'лишь', 'добро'] and next_el[0] == 'бы':
                concessive_sub += 1
            if is_have_grammar(next_el):
                d_next_el = process_grammar(next_el)
                d_next_el = d_next_el if d_next_el is not None else {}
                if el[0] in ['пусть', 'пускай'] and not (
                                d_next_el.get('pos') == 'V' and d_next_el.get('person') == '3'):
                    concessive_sub += 1
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if el[0] == 'хотя' and d_el.get('pos') == 'C':
                concessive_sub += 1
        else:
            continue
    return concessive_sub


# 35
# test that the sentence includes conditional subordinate clause
def conditional_subordinate(t):
    conditional_sub = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if el[0] in ['если', 'ежели', 'кабы', 'коль', 'коли', 'раз'] and d_el.get('pos') == 'C':
                conditional_sub += 1
        else:
            continue
    return conditional_sub


# 36
# test that the sentence includes purpose subordinate clause
def purpose_subordinate(t):
    purpose_sub = 0
    for i, el in enumerate(t):
        if el[0] == 'дабы':
            purpose_sub += 1
        if el[0] in ['чтобы', 'чтоб']:
            if i == 0:
                purpose_sub += 1
            else:
                flag_not_purpose = False
                if i > 0:
                    prev_el = t[i - 1]
                    if prev_el[2] in ['сомневаться', 'хотеть', 'захотеть', 'требовать', 'просить', 'желать',
                                      'ждать', 'мечтать', 'любить', 'загадать', 'захотеться', 'хотеться']:
                        flag_not_purpose = True
                if i - 1 > 0:
                    prev_el = t[i - 1]
                    prev_prev_el = t[i - 2]
                    if prev_el[0] == ',' and prev_prev_el[2] in ['сомневаться', 'хотеть', 'захотеть', 'требовать',
                                                                 'просить', 'желать', 'ждать', 'мечтать', 'любить',
                                                                 'загадать', 'захотеться', 'хотеться']:
                        flag_not_purpose = True
                    if (prev_el[2] in ['уверить', 'уверен', 'уверенный', 'верить', 'сказать', 'то'] and
                                prev_prev_el[0] == 'не'):
                        flag_not_purpose = True
                if i - 2 > 0:
                    prev_el = t[i - 1]
                    prev_prev_el = t[i - 2]
                    prev_prev_prev_el = t[i - 3]
                    if (prev_el[0] == ',' and
                                prev_prev_el[2] in ['уверенный', 'уверен', 'уверить', 'верить', 'сказать', 'то'] and
                                prev_prev_prev_el[0] == 'не'):
                        flag_not_purpose = True
                    if prev_el[2] == 'сказать' and prev_prev_el[2] == 'мочь' and prev_prev_prev_el[0] == 'не':
                        flag_not_purpose = True
                if i - 3 > 0:
                    prev_el = t[i - 1]
                    prev_prev_el = t[i - 2]
                    prev_prev_prev_el = t[i - 3]
                    prev_prev_prev_prev_el = t[i - 4]
                    if (prev_el[0] == ',' and prev_prev_el[2] == 'сказать' and prev_prev_prev_el[2] == 'мочь' and
                                prev_prev_prev_prev_el[0] == 'не'):
                        flag_not_purpose = True
                if not flag_not_purpose:
                    purpose_sub += 1
                else:
                    continue
    return purpose_sub


# 37
# test that the current word has a conditional mood form
def conditional_mood(t):
    cond = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'V' and d_el.get('vform') == 'c' or el[0] == 'бы':
                cond += 1
        else:
            continue
    return cond


# 38
# test that the current word is a modal word (possibility)
def modal_possibility(t):
    mod_pos = 0
    for i, el in enumerate(t):
        if el[2] in ['мочь'] or el[0] in ['по-видимому']:
            mod_pos += 1
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if i + 1 < len(t):
                next_el = t[i + 1]
                if ((el[0] == 'можно' and next_el[0] == 'быть') or
                        (el[0] == 'всей' and next_el[0] == 'вероятности') or
                        (el[0] == 'едва' and next_el[0] == 'ли') or
                        (el[0] == 'чуть' and next_el[0] == 'ли') or
                        (el[0] == 'вряд' and next_el[0] == 'ли')):
                    mod_pos += 1
            if d_el.get('pos') == 'R' and el[2] in ['наверное', 'наверно', 'возможно', 'видимо', 'верно', 'вероятно',
                                                    'пожалуй', 'можно']:
                mod_pos += 1
    return mod_pos


# 39
# test that the current word is a modal word (necessity)
def modal_necessity(t):
    mod_nec = 0
    for i, el in enumerate(t):
        d_el = process_grammar(el)
        if el[0] == 'требуется':
            mod_nec += 1
        if i + 1 < len(t):
            next_el = t[i + 1]
            if is_have_grammar(next_el):
                d_next_el = process_grammar(next_el)
                d_next_el = d_next_el if d_next_el is not None else {}
                if el[0] in ['следует', 'надлежит'] and d_next_el.get('pos') == 'V' and d_next_el.get('vform') == 'n':
                    mod_nec += 1
        if is_have_grammar(el):
            if d_el.get('pos') == 'R' and el[2] in ['нужно', 'надо', 'необходимо', 'нельзя', 'обязательно', 'неизбежно',
                                                    'непременно']:
                mod_nec += 1
            if el[2] in ['должный', 'обязанный'] and d_el.get('pos') == 'A' and d_el.get('definiteness') == 's':
                mod_nec += 1
    return mod_nec


# 40
# test that the current word is evaluative
def evaluative_vocabulary(t):
    eval = 0
    with codecs.open(r'dictionaries/evaluative_vocab.txt', mode='r', encoding='utf-8') as f:
        evaluative_words = set([s.strip() for s in f.readlines()])
    for i, el in enumerate(t):
        if el[2] in evaluative_words:
            eval += 1
    return eval


# 41
# test that the current word is academic
def academic_vocabulary(t):
    acad = 0
    with codecs.open(r'dictionaries/academic_words.txt', mode='r', encoding='utf-8') as f:
        academic_words = set([s.strip() for s in f.readlines()])
    for i, el in enumerate(t):
        if el[2] in academic_words:
            acad += 1
    return acad


# 42
# test that the sentence includes parenthesis with the meaning of attitude or evaluation
def parenthesis_attitude_evaluation(t):
    parent = 0
    for i, el in enumerate(t):
        flag = False
        if el[0] in ['увы', 'странно', 'удивительно', 'надеюсь', 'думаю', 'полагаю', 'пожалуй', 'думается', 'конечно',
                     'разумеется', 'бесспорно', 'действительно', 'положим', 'предположим', 'допустим', 'признаюсь']:
            if i + 1 < len(t):
                next_el = t[i + 1]
                if i == 0 and next_el[0] == ',':
                    flag = True
                if i > 0:
                    prev_el = t[i - 1]
                    if prev_el[0] == ',':
                        flag = True
        if el[0] in ['счастью', 'радости', 'удовольствию', 'несчастью', 'удивлению', 'сожалению', 'изумлению', 'стыду',
                     'досаде', 'неудовольствю', 'прискорбию', 'огорчению']:
            if i > 0:
                prev_el = t[i - 1]
                if prev_el[0] == 'к':
                    flag = True
            if i - 1 > 0:
                prev_prev_el = t[i - 2]
                if prev_prev_el[0] == 'к':
                    flag = True
        if i + 1 < len(t):
            next_el = t[i + 1]
            if i == 1 or (i - 1 > 0 and t[i - 2][0] == ','):
                prev_el = t[i - 1]
                if (el[0] in ['хорошо', 'хуже', 'плохо', 'хуже', 'обидно'] and prev_el[0] == 'что' or
                                el[0] in ['несчастью', 'правде', 'существу', 'сути'] and prev_el[0] == 'по' or
                                el[0] == 'дело' and prev_el[0] in ['странное', 'удивительное', 'непонятное'] or
                                el[0] == 'доброго' and prev_el[0] == 'чего' or el[0] == 'полагать' and prev_el[
                    0] == 'надо' or
                                el[0] == 'сомнения' and prev_el[0] == 'без' or el[0] == 'собой' and prev_el[
                    0] == 'само' or
                                el[0] == 'образом' and prev_el[0] == 'некоторым' or el[0] == 'хотите' and prev_el[
                    0] == 'если' or
                                el[0] == 'шуток' and prev_el[0] == 'кроме' or el[0] == 'скажу' and prev_el[
                    0] == 'прямо' or
                                el[0] == 'беду' and prev_el[0] == 'на' or el[0] == 'делом' and prev_el[
                    0] == 'грешным' or
                                el[0] == 'час' and prev_el[0] in ['неровен', 'неровён'] or el[0] == 'нарочно' and
                        prev_el[0] == 'как'):
                    if next_el[0] in [',', '.']:
                        flag = True
        if i + 1 < len(t):
            next_el = t[i + 1]
            if i == 2 or (i - 2 > 0 and t[i - 3][0] == ','):
                prev_el = t[i - 1]
                prev_prev_el = t[i - 2]
                if (el[0] == 'бог' and prev_el[0] == 'дай' and prev_prev_el[0] == 'не' or
                                    el[0] == 'разумеется' and prev_el[0] == 'собой' and prev_prev_el[0] == 'само' or
                                    el[0] == 'смысле' and prev_el[0] == 'каком-то' and prev_prev_el[0] == 'в' or
                                    el[0] == 'совести' and prev_el[0] == 'по' and prev_prev_el[0] == 'говоря' or
                                    el[0] == 'чести' and prev_el[0] == 'по' and prev_prev_el[0] == 'сказать' or
                                    el[0] == 'говоря' and prev_el[0] == 'нами' and prev_prev_el[0] == 'между' or
                                    el[0] == 'сказать' and prev_el[0] == 'правду' and prev_prev_el[0] == 'если' or
                                    el[0] == 'говоря' and prev_el[0] == 'правде' and prev_prev_el[0] == 'по' or
                                    el[0] == 'говоря' and prev_el[0] == 'сущности' and prev_prev_el[0] == 'в' or
                                    el[0] == 'говорить' and prev_el[0] == 'зря' and prev_prev_el[0] == 'нечего' or
                                    el[0] in ['хорошо', 'лучше', 'плохо', 'хуже'] and prev_el[0] == 'еще' and
                                prev_prev_el[0] == 'что'):
                    if next_el[0] in [',', '.']:
                        flag = True
        if flag:
            parent += 1
    return parent


# 43
# test that the current word is an animate noun
def animate_nouns(t):
    anim_nouns = 0
    with codecs.open('dictionaries/all_lemmas_animate_nouns.txt', mode='r', encoding='utf-8') as f:
        read_lines = set([s.strip().lower() for s in f.readlines()])
    for i, el in enumerate(t):
        if el[2] in read_lines:
            anim_nouns += 1
    return anim_nouns


# 44
# test that the sentence includes parenthesis with the meaning of accentuation
def parenthesis_accentuation(t):
    parent = 0
    for i, el in enumerate(t):
        flag = False
        if el[0] in ['повторяю', 'повторяем', 'подчеркиваю', 'подчеркиваем', 'представь', 'представьте', 'поверишь',
                     'поверите', 'вообрази', 'вообразите', 'согласись', 'согласитесь', 'заметь', 'заметьте', 'замечу',
                     'заметим', 'например', 'знаешь', 'знаете', 'значит', 'понимаешь', 'понимаете', 'главное',
                     'собственно', 'поверь', 'поверьте']:
            if i + 1 < len(t):
                next_el = t[i + 1]
                if i == 0 and next_el[0] == ',':
                    flag = True
                if i > 0:
                    prev_el = t[i - 1]
                    if prev_el[0] == ',':
                        flag = True
        if i + 1 < len(t):
            next_el = t[i + 1]
            if i == 1 or (i - 1 > 0 and t[i - 2][0] == ','):
                prev_el = t[i - 1]
                if (el[0] in ['важно', 'существенно'] and prev_el[0] == 'что' or
                                el[0] in ['поверишь', 'поверите'] and prev_el[0] == 'не' or
                                el[0] == 'дело' and prev_el[0] == 'главное' or
                                el[0] in ['напоминаю', 'напоминаем'] and prev_el[0] == 'как' or
                                el[0] == 'примеру' and prev_el[0] == 'к' or
                                el[0] == 'сказать' and prev_el[0] == 'так' or
                                el[0] in ['вам', 'тебе'] and prev_el[0] == 'скажу' or
                                el[0] == 'сказать' and prev_el[0] == 'надо' or
                                el[0] == 'общем' and prev_el[0] == 'в' or
                                el[0] == 'говоря' and prev_el[0] == 'собственно'):
                    if next_el[0] in [',', '.']:
                        flag = True
        if i + 1 < len(t):
            next_el = t[i + 1]
            if i == 2 or (i - 2 > 0 and t[i - 3][0] == ','):
                prev_el = t[i - 1]
                prev_prev_el = t[i - 2]
                if (el[0] in ['важнее', 'существеннее'] and prev_el[0] == 'еще' and prev_prev_el[0] == 'что' or
                                    el[0] == 'представить' and prev_el[0] == 'себе' and prev_prev_el[0] in ['можешь',
                                                                                                            'можете']):
                    if next_el[0] in [',', '.']:
                        flag = True
        if flag:
            parent += 1
    return parent


# 45
# test that the sentence includes parenthesis with the meaning of relation
def parenthesis_relation(t):
    parent = 0
    for i, el in enumerate(t):
        flag = False
        if el[0] in ['вдобавок', 'притом', 'следовательно', 'напротив', 'наоборот', 'во-первых', 'во-вторых',
                     'в-третьих', 'в-четвертых', 'в-пятых', 'в-шестых', 'в-седьмых', 'в-восьмых', 'в-девятых',
                     'в-десятых', 'значит', 'кстати', 'главное']:
            if i + 1 < len(t):
                next_el = t[i + 1]
                if i == 0 and next_el[0] == ',':
                    flag = True
                if i > 0:
                    prev_el = t[i - 1]
                    if prev_el[0] == ',':
                        flag = True
        if i + 1 < len(t):
            next_el = t[i + 1]
            if i == 1 or (i - 1 > 0 and t[i - 2][0] == ','):
                prev_el = t[i - 1]
                if (el[0] == 'того' and prev_el[0] in ['кроме', 'сверх'] or
                                el[0] == 'быть' and prev_el[0] == 'стало' or
                                el[0] == 'более' and prev_el[0] == 'тем' or
                                el[0] in ['водится', 'повелось', 'всегда'] and prev_el[0] == 'как' or
                                el[0] in ['обычаю', 'обыкновению'] and prev_el[0] == 'по' or
                                el[0] in ['твоя', 'ваша'] and prev_el[0] == 'воля' or
                                el[0] == 'воля' and prev_el[0] in ['твоя', 'ваша'] or
                                el[0] == 'быть' and prev_el[0] == 'стало' or
                                el[0] == 'того' and prev_el[0] in ['мало', 'сверх', 'помимо']):
                    if next_el[0] in [',', '.']:
                        flag = True
        if i + 1 < len(t):
            next_el = t[i + 1]
            if i == 2 or (i - 2 > 0 and t[i - 3][0] == ','):
                prev_el = t[i - 1]
                prev_prev_el = t[i - 2]
                if (el[0] == 'же' and prev_el[0] == 'тому' and prev_prev_el[0] == 'к' or
                                    el[0] == 'всего' and prev_el[0] == 'довершение' and prev_prev_el[0] == 'в' or
                                    el[0] == 'хочешь' and prev_el[0] == 'ты' and prev_prev_el[0] == 'как' or
                                    el[0] == 'же' and prev_el[0] == 'тому' and prev_prev_el[0] == 'же' or
                                    el[0] == 'концов' and prev_el[0] == 'конце' and prev_prev_el[0] == 'в'):
                    if next_el[0] in [',', '.']:
                        flag = True
        if flag:
            parent += 1
    return parent


# 46
# test that the current word is an adverb with the meaning of degree
def degree_adverb(t):
    degree = 0
    for i, el in enumerate(t):
        if el[0] in ['чересчур', 'втрое', 'вчетверо', 'впятеро', 'вшестеро', 'всемеро', 'вдесятеро', 'чуть-чуть',
                     'невыразимо', 'несказанно', 'беспредельно', 'безмерно', 'невыносимо', 'феноменально',
                     'сверхъестественно', 'едва-едва']:
            degree += 1
        if i + 1 < len(t):
            next_el = t[i + 1]
            if is_have_grammar(next_el):
                d_next_el = process_grammar(next_el)
                d_next_el = d_next_el if d_next_el is not None else {}
                if el[0] == 'несколько' and d_next_el.get('pos') == 'A':
                    degree += 1
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'R' and el[0] in ['крайне', 'очень', 'страшно', 'удивительно', 'исключительно',
                                                    'слишком', 'гораздо', 'абсолютно', 'совершенно', 'необычно',
                                                    'весьма', 'совсем', 'настолько', 'вдвое', 'еле', 'еле-еле',
                                                    'немного', 'необыкновенно', 'необычайно', 'фантастически',
                                                    'чрезвычайно', 'бешено', 'чудовищно', 'неслыханно', 'божественно',
                                                    'бесконечно', 'безумно', 'смертельно', 'ослепительно', 'нестерпимо',
                                                    'блестяще', 'гениально', 'сравнительно', 'относительно',
                                                    'невероятно', 'едва', 'капельку']:
                degree += 1
    return degree


# 47
# test that the current word is a particle
def particles(t):
    particle = 0
    for i, el in enumerate(t):
        flag = False
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'Q' and el[0] in ['же', 'ну', 'прямо', 'уж', 'вот', 'там', 'разве', 'ли', 'вроде',
                                                    'ж', 'дай', 'только', 'ведь', 'даже', 'лишь']:
                flag = True
        if el[0] in ['таки', 'ка', 'то-то']:
            flag = True
        if i + 1 < len(t):
            next_el = t[i + 1]
            if is_have_grammar(next_el):
                d_next_el = process_grammar(next_el)
                d_next_el = d_next_el if d_next_el is not None else {}
                if ((el[0] == 'так' and next_el[0] == 'и') or
                        (el[2] in ['какой', 'куда', 'где'] and next_el[0] == 'там' and d_next_el.get('pos') == 'Q') or
                        (el[0] == 'как' and next_el[0] == 'есть') or
                        (el[0] == 'знай' and next_el[0] == 'себе') or
                        (el[0] == 'едва' and next_el[0] == 'не') or
                        (el[0] == 'как' and next_el[0] == 'раз') or
                        (el[0] == 'чуть' and next_el[0] == 'не') or
                        (el[0] == 'нет-нет' and next_el[0] == 'и')):
                    flag = True
        if i + 2 < len(t):
            next_el = t[i + 1]
            next_next_el = t[i + 2]
            if ((el[0] == 'не' and next_el[0] == 'то' and next_next_el[0] in ['чтоб', 'чтобы']) or
                    (el[0] == 'не' and next_el[0] == 'иначе' and next_next_el[0] in ['как', 'чтобы']) or
                    (el[0] == 'чуть' and next_el[0] == 'было' and next_next_el[0] == 'не') or
                    (el[0] == 'того' and next_el[0] == 'и' and next_next_el[0] in ['гляди', 'жди']) or
                    (el[0] == 'нет-нет' and next_el[0] == 'да' and next_next_el[0] == 'и') or
                    (el[0] == 'ни' and next_el[0] == 'на' and next_next_el[0] == 'есть')):
                flag = True
        if flag:
            particle += 1
    return particle


# 48
# test that the current word is a numeral
def numeral(t):
    num = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'M':
                num += 1
    return num


# 49
# test that the current word in or not in the list of top 100 most frequent nouns
def top_100_nouns(t):
    top_nouns = 0
    not_top = 0
    with codecs.open('frequency_dict/frequent_nouns_top_100.txt', mode='r', encoding='utf-8') as f:
        read_lines = set([s.strip().lower() for s in f.readlines()])
    for i, el in enumerate(t):
        if el[2] in read_lines:
            top_nouns += 1
        else:
            not_top += 1
    return top_nouns, not_top


# 50
# test that the current word in or not in the list of top 1000 most frequent nouns (without the first top 100)
def top_1000_nouns_minus_head(t):
    nouns_minus_head = 0
    not_top = 0
    with codecs.open('frequency_dict/frequent_nouns_minus_head_100.txt', mode='r', encoding='utf-8') as f:
        read_lines = set([s.strip().lower() for s in f.readlines()])
    for i, el in enumerate(t):
        if el[2] in read_lines:
            nouns_minus_head += 1
        else:
            not_top += 1
    return nouns_minus_head, not_top


# 51
# test that the current word in or not in the list of top 100 most frequent verbs
def top_100_verbs(t):
    top_verbs = 0
    not_top = 0
    with codecs.open('frequency_dict/frequent_verbs_top_100.txt', mode='r', encoding='utf-8') as f:
        read_lines = set([s.strip().lower() for s in f.readlines()])
    for i, el in enumerate(t):
        if el[2] in read_lines:
            top_verbs += 1
        else:
            not_top += 1
    return top_verbs, not_top


# 52
# test that the current word in or not in the list of top 100 most frequent verbs (without 100 top verbs)
def top_1000_verbs_minus_head(t):
    verbs_minus_head = 0
    not_top = 0
    with codecs.open('frequency_dict/frequent_verbs_minus_head_100.txt', mode='r', encoding='utf-8') as f:
        read_lines = set([s.strip().lower() for s in f.readlines()])
    for i, el in enumerate(t):
        if el[2] in read_lines:
            verbs_minus_head += 1
        else:
            not_top += 1
    return verbs_minus_head, not_top


# 53
# test that the current not in the list of top 100 most frequent words
def top_100(t):
    top_100 = 0
    with codecs.open('frequency_dict/top_100_freq.txt', mode='r', encoding='utf-8') as f:
        read_lines = set([s.strip().lower() for s in f.readlines()])
    for i, el in enumerate(t):
        if el[2] not in read_lines:
            top_100 += 1
    return top_100


# 54
# test that the current not in the list of top 300 most frequent words
def top_300(t):
    top_300 = 0
    with codecs.open('frequency_dict/top_300_freq.txt', mode='r', encoding='utf-8') as f:
        read_lines = set([s.strip().lower() for s in f.readlines()])
    for i, el in enumerate(t):
        if el[2] not in read_lines:
            top_300 += 1
    return top_300


# 55
# test that the current not in the list of top 500 most frequent words
def top_500(t):
    top_500 = 0
    with codecs.open('frequency_dict/top_500_freq.txt', mode='r', encoding='utf-8') as f:
        read_lines = set([s.strip().lower() for s in f.readlines()])
    for i, el in enumerate(t):
        if el[2] not in read_lines:
            top_500 += 1
    return top_500


# 56
# test that the current not in the list of top 10000 most frequent words
def top_10000(t):
    top_10000 = 0
    with codecs.open('frequency_dict/top_10000.txt', mode='r', encoding='utf-8') as f:
        read_lines = set([s.strip().lower() for s in f.readlines()])
        for i, el in enumerate(t):
            if el[2] not in read_lines:
                top_10000 += 1
    return top_10000


# 57
# test that the current not in the list of top 5000 most frequent words
def top_5000(t):
    top_5000 = 0
    with codecs.open('frequency_dict/top_5000.txt', mode='r', encoding='utf-8') as f:
        read_lines = set([s.strip().lower() for s in f.readlines()])
        for i, el in enumerate(t):
            if el[2] not in read_lines:
                top_5000 += 1
    return top_5000


# 58
# test that the current word has a complex ending (like приборостро-ение)
def complex_endings(t):
    end = 0
    for el in t:
        lemma = el[2]
        if len(lemma) > 5:
            if lemma[-5:] in ['ствие', 'енный', 'вание', 'льный', 'ность', 'еский', 'нение', 'шение',
                              'ление', 'оящий', 'жение']:
                end += 1
            elif lemma[-4:] in ['ение', 'ание', 'ьный', 'ость', 'нный', 'ация', 'ский', 'твие', 'ящий']:
                end += 1
            elif lemma[-3:] in ['ние', 'ный', 'сть', 'ция', 'вие']:
                end += 1
            elif lemma[-2:] in ['ие', 'ый', 'ия']:
                end += 1
    return end


# 59
# test that it is a finite verb of 1st or 2nd person
def is_12person_verb(t):
    verb = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'V' and (d_el.get('person') == '1' or d_el.get('person') == '2'):
                verb += 1
        else:
            continue
    return verb
