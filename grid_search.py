import numpy as np
from sklearn.grid_search import GridSearchCV


def grid_estimation(model, data, target):
    # prepare a range of alpha values to test
    gammas = np.array([1, 0.1, 0.01, 0.001, 0.0001])
    cs = np.array([1, 10, 100, 1000])
    # create and fit a ridge regression model, testing each alpha
    grid = GridSearchCV(estimator=model, param_grid=dict(gamma=gammas, C=cs))
    grid.fit(data, target)

    return grid.best_score_, grid.best_estimator_.gamma, grid.best_estimator_.C
