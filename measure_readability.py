# -*- coding: utf-8 -*-
import codecs
from parse_corpus_rftagger import parse_text_by_tagger
import os
from sklearn.externals import joblib

clf = joblib.load('classifier_data\\model.pkl')
scaler = joblib.load('classifier_data\\scaler.pkl')
normalizer = joblib.load('classifier_data\\normalizer.pkl')

# the directory where you should put your txt files to measure readability
#test_texts_dir = 'test_texts'
test_texts_dir = input('Name of the dir with your texts:')

for filename in os.listdir(test_texts_dir):
    file_path = os.path.join(test_texts_dir, filename)
    with codecs.open(file_path, mode='r', encoding='utf-8') as f:
        text = f.read()
        (features, grades) = parse_text_by_tagger(text)
        feature_vector = [features]

        data = normalizer.transform(feature_vector)
        data = scaler.transform(data)
        complexity_mean_grade = grades[6]

        prediction = clf.predict(data)
        print(filename)
        if prediction[0] == 1.0:
            if complexity_mean_grade > 20:
                print('middle')
            else:
                print('easy')
        elif prediction[0] == 2.0:
            if complexity_mean_grade > 24:
                print('hard')
            else:
                print('middle')
        elif prediction[0] == 3.0:
            print('hard')

        print("Metric Flesh Kincaid: {0:.2f}".format(grades[0]))
        print("Metric Flesh Kincaid flex: {0:.2f}".format(grades[1]))
        print("Metric Coleman Liau: {0:.2f}".format(grades[2]))
        print("Metric SMOG: {0:.2f}".format(grades[3]))
        print("Metric Dale Chale: {0:.2f}".format(grades[4]))
        print("Metric Automated Readability Index (ARI): {0:.2f}".format(grades[5]))
        print("Median on all metrics: {0:.2f}".format(complexity_mean_grade))
        print()





