import numpy as np
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.metrics import confusion_matrix

from svm_plot import plot_svm_decision_boundary, plot_score_vs_degree, plot_score_vs_gamma, plot_mnist, \
    plot_confusion_matrix

"""
Assignment 4: Support Vector Machine, Kernels & Multiclass classification
TODOS are contained here.
"""


def ex_1_a(x, y):
    """
    Solution for exercise 1 a)
    :param x: The x values
    :param y: The y values
    :return:
    """
    ###########
    ## TODO:
    ## Train an SVM with a linear kernel
    ## and plot the decision boundary and support vectors using 'plot_svm_decision_boundary' function
    ###########

    clf = svm.SVC(kernel='linear')
    clf.fit(x, y)

    plot_svm_decision_boundary(clf, x, y)


def ex_1_b(x, y):
    """
    Solution for exercise 1 b)
    :param x: The x values
    :param y: The y values
    :return:
    """
    ###########
    ## TODO:
    ## Add a point (4,0) with label 1 to the data set and then
    ## train an SVM with a linear kernel
    ## and plot the decision boundary and support vectors using 'plot_svm_decision_boundary' function
    ###########

    new_x = (4, 0)
    new_y = 1

    x = np.vstack([x, new_x])
    y = np.hstack([y, new_y])

    ex_1_a(x, y)


def ex_1_c(x, y):
    """
    Solution for exercise 1 c)
    :param x: The x values
    :param y: The y values
    :return:
    """
    ###########
    ## TODO:
    ## Add a point (4,0) with label 1 to the data set and then
    ## train an SVM with a linear kernel with different values of C
    ## and plot the decision boundary and support vectors  for each using 'plot_svm_decision_boundary' function
    ###########
    Cs = [1e6, 1, 0.1, 0.001]

    new_x = (4, 0)
    new_y = 1

    x = np.vstack([x, new_x])
    y = np.hstack([y, new_y])

    for C in Cs:
        clf = svm.SVC(kernel='linear', C=C)
        clf.fit(x, y)
        plot_svm_decision_boundary(clf, x, y)




def ex_2_a(x_train, y_train, x_test, y_test):
    """
    Solution for exercise 2 a)
    :param x_train: Training samples (2-dimensional)
    :param y_train: Training labels
    :param x_test: Testing samples (2-dimensional)
    :param y_test: Testing labels
    :return:
    """
    ###########
    ## Train an SVM with a linear kernel for the given dataset
    ## and plot the decision boundary and support vectors  for each using 'plot_svm_decision_boundary' function
    ###########

    clf = svm.SVC(kernel='linear')
    clf.fit(x_train, y_train)
    plot_svm_decision_boundary(clf, x_train, y_train, x_test, y_test)
    print("ex_2_a score:", clf.score(x_test, y_test))

    pass


def ex_2_b(x_train, y_train, x_test, y_test):
    """
    Solution for exercise 2 b)
    :param x_train: Training samples (2-dimensional)
    :param y_train: Training labels
    :param x_test: Testing samples (2-dimensional)
    :param y_test: Testing labels
    :return:
    """
    ###########
    ## TODO:
    ## Train SVMs with polynomial kernels for different values of the degree
    ## (Remember to set the 'coef0' parameter to 1)
    ## and plot the variation of the training and test scores with polynomial degree using 'plot_score_vs_degree' func.
    ## Plot the decision boundary and support vectors for the best value of degree
    ## using 'plot_svm_decision_boundary' function
    ###########
    degrees = range(1, 21)

    test_scores = np.array([])
    train_scores = np.array([])
    best_svm = None
    best_test_score = 0

    for deg in degrees:
        clf = svm.SVC(kernel='poly', degree=deg, coef0=1)
        clf.fit(x_train, y_train)

        test_score = clf.score(x_test, y_test)

        if test_score > best_test_score:
            best_test_score = test_score
            best_svm = clf

        test_scores  = np.append(test_scores, test_score)
        train_scores = np.append(train_scores, clf.score(x_train, y_train))

    plot_score_vs_degree(train_scores, test_scores, degrees)

    plot_svm_decision_boundary(clf, x_train, y_train, x_test, y_test)


def ex_2_c(x_train, y_train, x_test, y_test):
    """
    Solution for exercise 2 c)
    :param x_train: Training samples (2-dimensional)
    :param y_train: Training labels
    :param x_test: Testing samples (2-dimensional)
    :param y_test: Testing labels
    :return:
    """
    ###########
    ## TODO:
    ## Train SVMs with RBF kernels for different values of the gamma
    ## and plot the variation of the test and training scores with gamma using 'plot_score_vs_gamma' function.
    ## Plot the decision boundary and support vectors for the best value of gamma
    ## using 'plot_svm_decision_boundary' function
    ###########
    gammas = np.arange(0.01, 2, 0.02)

    test_scores = np.array([])
    train_scores = np.array([])
    best_svm = None
    best_test_score = 0

    for gamma in gammas:
        clf = svm.SVC(kernel='rbf', gamma=gamma)
        clf.fit(x_train, y_train)

        test_score = clf.score(x_test, y_test)

        if test_score > best_test_score:
            best_test_score = test_score
            best_svm = clf

        test_scores  = np.append(test_scores, test_score)
        train_scores = np.append(train_scores, clf.score(x_train, y_train))

    plot_score_vs_gamma(train_scores, test_scores, gammas)

    plot_svm_decision_boundary(clf, x_train, y_train, x_test, y_test)


def ex_3_a(x_train, y_train, x_test, y_test):
    """
    Solution for exercise 3 a)
    :param x_train: Training samples (2-dimensional)
    :param y_train: Training labels
    :param x_test: Testing samples (2-dimensional)
    :param y_test: Testing labels
    :return:
    """
    ###########
    ## TODO:
    ## Train multi-class SVMs with one-versus-rest strategy with
    ## - linear kernel
    ## - rbf kernel with gamma going from 10**-5 to 10**5
    ## - plot the scores with varying gamma using the function plot_score_versus_gamma
    ## - Note that the chance level is not .5 anymore and add the score obtained with the linear kernel as optional argument of this function (parameter baseline)
    ###########

    gamma_range = [10**-5, 10**-4, 10**-3, 10**-2, 10**-1, 10**0, 10**1, 10**2, 10**3, 10**4, 10**5]

    lin = svm.SVC(decision_function_shape='ovr', kernel='linear', C=10)
    lin.fit(x_train, y_train)

    score_train = lin.score(x_train, y_train)
    score_test = lin.score(x_test, y_test)

    gam_score_train = []
    gam_score_test = []
    for gamma_value in gamma_range:
        gam = svm.SVC(decision_function_shape='ovr', kernel='rbf', gamma=gamma_value, C=10)
        gam.fit(x_train, y_train)

        gam_score_train.append(gam.score(x_train, y_train))
        gam_score_test.append(gam.score(x_test, y_test))

    plot_score_vs_gamma(gam_score_train, gam_score_test, gamma_range, score_train, score_test, baseline=0.2)


def ex_3_b(x_train, y_train, x_test, y_test):
    """
    Solution for exercise 3 b)
    :param x_train: Training samples (2-dimensional)
    :param y_train: Training labels
    :param x_test: Testing samples (2-dimensional)
    :param y_test: Testing labels
    :return:
    """
    ###########
    ## TODO:
    ## Train multi-class SVMs with a LINEAR kernel
    ## Use the sklearn.metrics.confusion_matrix to plot the confusion matrix.
    ## Find the index for which you get the highest error rate.
    ## Plot the confusion matrix with plot_confusion_matrix.
    ## Plot the first 10 images classified as the most misclassified digit using plot_mnist.
    ###########

    labels = range(1, 6)

    lin = svm.SVC(decision_function_shape='ovr', kernel='linear')
    lin.fit(x_train, y_train)

    y_test_predict =lin.predict(x_test)

    score_train = lin.score(x_train, y_train)
    score_test = lin.score(x_test, y_test)

    cm = confusion_matrix(y_test, y_test_predict)
    plot_confusion_matrix(cm, labels)
    #print(cm)

    diff_list = y_test_predict == y_test

    # indexes of all missclassiefied images
    misclassifieds = [i for i, val in enumerate(diff_list) if val == False]

    # remove diagonal elements from cm for later processing
    cm_no_diagonal = cm
    np.fill_diagonal(cm_no_diagonal, 0)
    #print(cm_no_diagonal)

    errors_per_class = np.sum(cm_no_diagonal, axis=0)
    #print(errors_per_class)

    sel_err = np.array(misclassifieds)  # CHANGE ME! Numpy indices to select all images that are misclassified.
    i = np.argmax(errors_per_class)  # CHANGE ME! Should be the label number corresponding the largest classification error.
    #print(i)

    # Plot with mnist plot
    plot_mnist(x_test[sel_err], y_test_predict[sel_err], labels=labels[i], k_plots=10, prefix='Predicted class')
