# -*- coding: utf-8 -*-
import os
import codecs
from tagger import rfttag
import feature_extractors
import csv
import metrics

# the directory with text for training of classifier
input_root = "C:\\Users\\Askinkaty\\PycharmProjects\\TextReadability\\out_dir"


# function for tagging input txt file, parsing features and counting
def parse_text_by_tagger(input_text):
    values = []
    grades = []
    first_person_pronoun = 0
    second_person_pronoun = 0
    third_person_pronoun = 0
    pronoun = 0
    finite_verb = 0
    modifier = 0
    past_tense = 0
    perf_aspect = 0
    present_tense = 0
    total_adverb = 0
    nominalization = 0
    all_nouns = 0
    genitive = 0
    neuter = 0
    passive = 0
    infin = 0
    speech_verb = 0
    mental_verb = 0
    that_complements = 0
    wh_relatives = 0
    total_pp = 0
    word_length = 0
    all_syllables = 0
    all_complex_words = 0
    complex_words = 0
    word_complexity = 0
    all_letters = 0
    all_words = 0
    text_span = 0
    sent_span = 0
    sentence_length = 0
    all_sent_words = 0
    all_sent_marks = 0
    type_token_ratio = 0
    all_types = set()
    all_tokens = 0
    verbal_adverb = 0
    passive_participial_clauses = 0
    active_participial_clauses = 0
    imperative = 0
    predicative_adjectives = 0
    attributive_adjective = 0
    causative_subordinate = 0
    concessive_subordinate = 0
    conditional_subordinate = 0
    purpose_subordinate = 0
    conditional_mood = 0
    modal_possibility = 0
    modal_necessity = 0
    evaluative_vocabulary = 0
    academic_vocabulary = 0
    parenthesis_attitude = 0
    animate = 0
    parenthesis_accentuation = 0
    parenthesis_relation= 0
    degree_advert = 0
    particles = 0
    numeral = 0
    top_100_nouns = 0
    non_top_100_nouns = 0
    nouns_minus_head = 0
    non_nouns_minus_head = 0
    top_100_verbs = 0
    non_top_100_verbs = 0
    verbs_minus_head = 0
    non_verbs_minus_head = 0
    top_100 = 0
    top_300 = 0
    top_500 = 0
    top_10000 = 0
    top_5000 = 0
    complex_endings = 0
    fsperson_verb = 0
    fk_grade = 0
    fk_grade_flex = 0
    cl_grade = 0
    smog_grage = 0
    dale_grade = 0
    ari_index = 0
    complexity_grade = 0


    tagged_text = rfttag(input_text)
    for tagged_sent in tagged_text:
        tagged_sent = [(el[0].lower(), el[1], el[2].lower()) for el in tagged_sent]

        first_person_pronoun += feature_extractors.first_person_pronoun(tagged_sent)
        second_person_pronoun += feature_extractors.second_person_pronoun(tagged_sent)
        # third_person_pronoun += feature_extractors.third_person_pronoun(tagged_sent)
        pronoun += feature_extractors.is_pronoun(tagged_sent)
        finite_verb += feature_extractors.is_finite_verb(tagged_sent)
        modifier += feature_extractors.is_modifier(tagged_sent)
        # past_tense += feature_extractors.past_tense(tagged_sent)
        # perf_aspect += feature_extractors.perf_aspect(tagged_sent)
        # present_tense += feature_extractors.present_tense(tagged_sent)
        total_adverb += feature_extractors.total_adverb(tagged_sent)
        (nomz, nouns) = feature_extractors.is_nominalization(tagged_sent)
        nominalization += nomz
        # all_nouns += nouns
        genitive += feature_extractors.is_genitive(tagged_sent)
        # neuter += feature_extractors.is_neuter(tagged_sent)
        passive += feature_extractors.is_passive(tagged_sent)
        # infin += feature_extractors.infinitives(tagged_sent)
        speech_verb += feature_extractors.speech_verb(tagged_sent)
        mental_verb += feature_extractors.mental_verb(tagged_sent)
        # that_complements += feature_extractors.that_complement(tagged_sent)
        # wh_relatives += feature_extractors.wh_relatives(tagged_sent)
        # total_pp += feature_extractors.total_PP(tagged_sent)
        (letters, words) = feature_extractors.word_length(tagged_sent)
        all_letters += letters
        all_words += words
        (syllables, complex_words) = feature_extractors.syllables(tagged_sent)
        all_syllables += syllables
        all_complex_words += complex_words
        sent_words = feature_extractors.sentence_length(tagged_sent)
        all_sent_words += sent_words
        all_sent_marks += 1
        sent_span += feature_extractors.text_span(tagged_sent)
        (types, tokens) = feature_extractors.type_token_ratio(tagged_sent)
        all_types = all_types.union(types)
        all_tokens += tokens
        verbal_adverb += feature_extractors.is_verbal_adverb(tagged_sent)
        passive_participial_clauses += feature_extractors.passive_participial_clauses(tagged_sent)
        active_participial_clauses += feature_extractors.active_participial_clauses(tagged_sent)
        imperative += feature_extractors.imperative_mood(tagged_sent)
        # predicative_adjectives += feature_extractors.predicative_adjectives(tagged_sent)
        # attributive_adjective += feature_extractors.attributive_adjective(tagged_sent)
        causative_subordinate += feature_extractors.causative_subordinate(tagged_sent)
        # concessive_subordinate += feature_extractors.concessive_subordinate(tagged_sent)
        # conditional_subordinate += feature_extractors.conditional_subordinate(tagged_sent)
        # purpose_subordinate += feature_extractors.purpose_subordinate(tagged_sent)
        # modal_possibility += feature_extractors.modal_possibility(tagged_sent)
        # modal_necessity += feature_extractors.modal_necessity(tagged_sent)
        # evaluative_vocabulary += feature_extractors.evaluative_vocabulary(tagged_sent)
        academic_vocabulary += feature_extractors.academic_vocabulary(tagged_sent)
        parenthesis_attitude += feature_extractors.parenthesis_attitude_evaluation(tagged_sent)
        # animate += feature_extractors.animate_nouns(tagged_sent)
        parenthesis_accentuation += feature_extractors.parenthesis_accentuation(tagged_sent)
        # parenthesis_relation += feature_extractors.parenthesis_relation(tagged_sent)
        degree_advert += feature_extractors.degree_adverb(tagged_sent)
        particles += feature_extractors.particles(tagged_sent)
        # numeral += feature_extractors.numeral(tagged_sent)
        # (t100nouns, non100nouns) = feature_extractors.top_100_nouns(tagged_sent)
        # top_100_nouns += t100nouns
        # non_top_100_nouns += non100nouns
        (t1000nouns, non1000nouns) = feature_extractors.top_1000_nouns_minus_head(tagged_sent)
        nouns_minus_head += t1000nouns
        # non_nouns_minus_head += non1000nouns
        (t100verbs, non100verbs) = feature_extractors.top_100_verbs(tagged_sent)
        top_100_verbs += t100verbs
        # non_top_100_verbs += non100verbs
        # (t1000verbs, non1000verbs) = feature_extractors.top_1000_verbs_minus_head(tagged_sent)
        # verbs_minus_head += t1000verbs
        # non_verbs_minus_head += non1000verbs
        # top_100 += feature_extractors.top_100(tagged_sent)
        # top_300 += feature_extractors.top_300(tagged_sent)
        # top_500 += feature_extractors.top_500(tagged_sent)
        # top_10000 += feature_extractors.top_10000(tagged_sent)
        top_5000 += feature_extractors.top_5000(tagged_sent)
        complex_endings += feature_extractors.complex_endings(tagged_sent)
        fsperson_verb += feature_extractors.is_12person_verb(tagged_sent)

    sentence_length = all_sent_words / all_sent_marks
    type_token_ratio = len(all_types) / all_tokens
    word_length = all_letters / all_words
    word_count = all_words
    word_complexity = all_syllables / all_words
    text_span = sent_span / all_sent_marks

# computing grades and indexes by formulas
    fk_grade = metrics.calc_Flesh_Kincaid_Grade_rus(all_syllables, word_count, all_sent_marks)
    fk_grade_flex = metrics.calc_Flesh_Kincaid_Grade_rus_flex(all_syllables, word_count, all_sent_marks)
    cl_grade = metrics.calc_Coleman_Liau_index(all_letters, word_count, all_sent_marks)
    smog_grage = metrics.calc_SMOG_index(all_complex_words, all_sent_marks)
    dale_grade = metrics.calc_Dale_Chale_index(all_complex_words, word_count, all_sent_marks)
    ari_index = metrics.calc_ARI_index(all_letters, word_count, all_sent_marks)
    complexity_grade = (fk_grade + fk_grade_flex + cl_grade + smog_grage + dale_grade + ari_index) / 6


    values.append(first_person_pronoun / word_count)
    values.append(second_person_pronoun / word_count)
    # values.append(third_person_pronoun / word_count)
    values.append(pronoun / word_count)
    values.append(finite_verb / word_count)
    values.append(modifier / word_count)
    # values.append(past_tense / word_count)
    # values.append(perf_aspect / word_count)
    # values.append(present_tense / word_count)
    values.append(total_adverb / word_count)
    values.append(nominalization / word_count)
    # values.append(all_nouns / word_count)
    values.append(genitive / word_count)
    # values.append(neuter / word_count)
    values.append(passive / word_count)
    # values.append(infin / word_count)
    values.append(speech_verb / word_count)
    values.append(mental_verb / word_count)
    # values.append(that_complements / word_count)
    # values.append(wh_relatives / word_count)
    # values.append(total_pp / word_count)
    # values.append(word_length)
    # values.append(word_complexity)
    values.append(text_span)
    values.append(sentence_length)
    values.append(type_token_ratio)
    values.append(verbal_adverb / word_count)
    values.append(passive_participial_clauses / word_count)
    values.append(active_participial_clauses / word_count)
    values.append(imperative / word_count)
    # values.append(predicative_adjectives / word_count)
    # values.append(attributive_adjective / word_count)
    values.append(causative_subordinate / word_count)
    # values.append(concessive_subordinate / word_count)
    # values.append(conditional_subordinate / word_count)
    # values.append(purpose_subordinate / word_count)
    # values.append(conditional_mood / word_count)
    # values.append(modal_possibility / word_count)
    # values.append(modal_necessity / word_count)
    # values.append(evaluative_vocabulary / word_count)
    values.append(academic_vocabulary / word_count)
    values.append(parenthesis_attitude / word_count)
    # values.append(animate / word_count)
    values.append(parenthesis_accentuation / word_count)
    # values.append(parenthesis_relation / word_count)
    values.append(degree_advert / word_count)
    values.append(particles / word_count)
    # values.append(numeral / word_count)
    # values.append(top_100_nouns / word_count)
    # values.append(non_top_100_nouns / word_count)
    values.append(nouns_minus_head / word_count)
    # values.append(non_nouns_minus_head / word_count)
    values.append(top_100_verbs / word_count)
    # values.append(non_top_100_verbs / word_count)
    # values.append(verbs_minus_head / word_count)
    # values.append(non_verbs_minus_head / word_count)
    # values.append(top_100 / word_count)
    # values.append(top_300 / word_count)
    # values.append(top_500 / word_count)
    # values.append(top_10000 / word_count)
    values.append(top_5000 / word_count)
    values.append(complex_endings / word_count)
    values.append(fsperson_verb / word_count)
    # values.append(fk_grade)
    # values.append(fk_grade_flex)
    # values.append(cl_grade)
    # values.append(smog_grage)
    # values.append(dale_grade)
    # values.append(ari_index)
    # values.append(complexity_grade)
    grades.append(fk_grade)
    grades.append(fk_grade_flex)
    grades.append(smog_grage)
    grades.append(cl_grade)
    grades.append(dale_grade)
    grades.append(ari_index)
    grades.append(complexity_grade)

    return values, grades



# the current file is run only if we build a matrix of training corpus saved in input directory
# the matrix of feature frequencies will be saved to out.csv
# you should choose which heading vector to write, it depends of the number of chosen features
# in the function parse_text_by_tagger(input_text)

if __name__ == '__main__':
    with open('out.csv', 'w', newline='\n') as csvfile:
        vectorwriter = csv.writer(csvfile)
        # vectorwriter.writerow(
        #         ['id', 'first_person_pronoun', 'second_person_pronoun', 'third_person_pronoun',
        #            'all_pronouns', 'finite_verbs', 'modifiers', 'past_tense', 'perf_aspect', 'present_tense',
        #            'total_adverb', 'nominalization', 'nouns', 'genitive', 'neuter', 'passive', 'infin',
        #             'speech_verb', 'mental_verb', 'that_compl', 'wh_relative',
        #            'total_PP', 'word_length', 'word_complexity', 'text_spans', 'sentence_length', 'type_token_ratio',
        #            'verbal_adverbs', 'passive_participial_clauses', 'active_participial_clauses',
        #            'imperative_mood', 'predicative_adjectives', 'attributive_adjective',
        #            'causative_subordinate', 'concessive_subordinate', 'conditional_subordinate',
        #            'purpose_subordinate', 'conditional_mood', 'modal_possibility', 'modal_necessity',
        #            'evaluative_vocabulary', 'academic vocabulary', 'parenthesis_attitude_evaluation', 'animate_nouns',
        #            'parenthesis_accentuation', 'parenthesis_relation', 'degree_adverb', 'particles',
        #             'numeral', 'top_100_nouns', 'non_top_100_nouns', 'top_1000_nouns_minus_head',
        #             'non_top_1000_nouns_minus_head', 'top_100_verbs', 'non_top_100_verbs', 'top_1000_verbs_minus_head',
        #             'non_top_1000_verbs_minus_head',
        #             'top_100', 'top_300', 'top_500', 'top_10000', 'top_5000', 'complex_endings',
        #             'first_second_person_verb', 'fk_grade',
        #             'fk_grade_flex', 'cl_grade', 'smog_grade', 'dale_grade', 'ari_index', 'complexity_grade'])

        vectorwriter.writerow (["first_person_pronoun","second_person_pronoun","all_pronouns","finite_verbs",
                                "modifiers","total_adverb","nominalization","genitive","passive","speech_verb",
                                "mental_verb","text_spans","sentence_length","type_token_ratio","verbal_adverbs",
                                "passive_participial_clauses","active_participial_clauses","imperative_mood",
                                "causative_subordinate","academic.vocabulary","parenthesis_attitude_evaluation",
                                "parenthesis_accentuation","degree_adverb","particles","top_1000_nouns_minus_head",
                                "top_100_verbs","top_5000","complex_endings","first_second_person_verb"])

        for name in os.listdir(input_root):
            filename = os.path.join(input_root, name)

            with codecs.open(filename, mode='r', encoding='utf-8') as f:
                text = f.read()
                vector = parse_text_by_tagger(text)
                name = os.path.basename(filename)
                vector.insert(0, name.split(".")[0])
                vectorwriter.writerow(vector)
                csvfile.flush()