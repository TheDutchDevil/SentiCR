from __future__ import print_function

from SentiCR import SentiCR, SentimentData
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import  precision_score
from sklearn.metrics import  f1_score

import  random
import csv
import re
import os
import codecs

import nltk
from xlrd import open_workbook
from statistics import mean


import numpy as np
import argparse

from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

from nltk.stem.snowball import SnowballStemmer
from imblearn.over_sampling import SVMSMOTE

from pkg_resources import resource_stream

def ten_fold_cross_validation(dataset,ALGO):
    kf = KFold(n_splits=10)

    run_precision = []
    run_recall = []
    run_f1score = []
    run_accuracy = []

    count=1

    #Randomly divide the dataset into 10 partitions
    # During each iteration one partition is used for test and remaining 9 are used for training
    for train, test in kf.split(dataset):
        print("Using split-"+str(count)+" as test data..")
        classifier_model=SentiCR(algo=ALGO,training_data= dataset[train])

        test_comments=[comments.text for comments in dataset[test]]
        test_ratings=[comments.rating for comments in dataset[test]]

        pred = classifier_model.get_sentiment_polarity_collection(test_comments)

        precision = precision_score(test_ratings, pred, pos_label=-1)
        recall = recall_score(test_ratings, pred, pos_label=-1)
        f1score = f1_score(test_ratings, pred, pos_label=-1)
        accuracy = accuracy_score(test_ratings, pred)

        run_accuracy.append(accuracy)
        run_f1score.append(f1score)
        run_precision.append(precision)
        run_recall.append(recall)
        count+=1

    return (mean(run_precision),mean(run_recall),mean(run_f1score),mean(run_accuracy))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Supervised sentiment classifier')

    parser.add_argument('--algo', type=str,
                        help='Classification algorithm', default="GBT")


    parser.add_argument('--repeat', type=int,
                        help='Iteration count', default=100)

    args = parser.parse_args()
    ALGO = args.algo
    REPEAT = args.repeat

    print("Cross validation")
    print("Algrithm: " + ALGO)
    print("Repeat: " + str(REPEAT))

    workbook = open_workbook("oracle.xlsx")
    sheet = workbook.sheet_by_index(0)
    oracle_data = []

    for cell_num in range(0, sheet.nrows):
        comments = SentimentData(sheet.cell(cell_num, 0).value,sheet.cell(cell_num, 1).value)
        oracle_data.append(comments)

    random.shuffle(oracle_data)

    oracle_data=np.array(oracle_data)

    Precision = []
    Recall = []
    Fmean = []
    Accuracy = []

    for k in range (0,REPEAT):
        print(".............................")
        print("Run# {}".format(k))
        (precision, recall, f1score, accuracy)=ten_fold_cross_validation(oracle_data,ALGO)
        Precision.append(precision)
        Recall.append(recall)
        Fmean.append(f1score)
        Accuracy.append(accuracy)
        print("Precision:"+str(precision))
        print("Recall:" + str(recall))
        print("F-measure:" + str(f1score))
        print("Accuracy:" + str(accuracy))

    ##########################
    training = open("cross-validation-" + ALGO + ".csv", 'w')
    training.write("Run,Algo,Precision,Recall,Fscore,Accuracy\n")

    for k in range(0, REPEAT):
        training.write(str(k) + "," + ALGO + "," + str(Precision[k]) + "," + str(Recall[k]) + "," +
                       str(Fmean[k]) + "," + str(Accuracy[k]) + "\n")
    training.close()

    print("-------------------------")
    print("Average Precision: {}".format(mean(Precision)))
    print("Average Recall: {}".format(mean(Recall)))
    print("Average Fmean: {}".format(mean(Fmean)))
    print("Average Accuracy: {}".format(mean(Accuracy)))
    print("-------------------------")
