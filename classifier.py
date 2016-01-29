# -*- coding: utf-8 -*-

from numpy import genfromtxt
from sklearn import cross_validation
from sklearn import svm
from sklearn import metrics
from sklearn.preprocessing import StandardScaler, Normalizer
from sklearn.externals import joblib
from grid_search import grid_estimation

# downloading matrix of text features and assigned clusters
all_data = genfromtxt('features_and_clusters.csv', delimiter=',')

data = all_data[:, 0:29]
target = all_data[:, 29]

# normalization and scaling of data
normalizer = Normalizer()
normalizer.fit(data)
data = normalizer.transform(data)
scaler = StandardScaler()
data = scaler.fit_transform(data)

# choosing of training and test sets
X_train, X_test, y_train, y_test = cross_validation.train_test_split(data, target, test_size=0.4, random_state=0)

#clf = svm.SVC(kernel="rbf", gamma=0.001, C=1000).fit(X_train, y_train)
clf = svm.SVC(kernel="linear", gamma=1.0, C=1).fit(X_train, y_train)

# saving of classifier, scaler and normalizer
joblib.dump(clf, 'classifier_data\\model.pkl')
joblib.dump(scaler, 'classifier_data\\scaler.pkl')
joblib.dump(normalizer, 'classifier_data\\normalizer.pkl')


# results of training and testing
if __name__ == '__main__':
    print(clf)
    print(clf.score(X_test, y_test))

    scores = cross_validation.cross_val_score(clf, data, target, cv=5)
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    predicted = cross_validation.cross_val_predict(clf, data, target, cv=10)
    print(metrics.accuracy_score(target, predicted))
    print(metrics.classification_report(target, predicted))
    print(metrics.confusion_matrix(target, predicted))

# function for a grid search of the best parameters of a classifier
    #print(grid_estimation(clf, data, target))

