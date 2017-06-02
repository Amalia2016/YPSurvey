# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import scipy as sc
import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold, train_test_split, cross_val_score
from sklearn.model_selection import train_test_split, ShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
    

def get_data():

    df = pd.read_csv("responses.csv")
    df1 = df.copy()
    # clean missing values
    drop_list = ['Gender','Left - right handed','Education','Only child','Village - town','House - block of flats',
             'Finances','Smoking', 'Alcohol', 'Punctuality', 'Lying', 'Internet usage']
    df1.dropna(subset= drop_list, inplace=True)
    df1.fillna(0, inplace=True)
    #
    mycolumns = ['Finances', 'Prioritising workload','Keeping promises', 'Decision making', 'Thinking ahead', 'Questionnaires or polls', 'Getting up', 'Entertainment spending', 'Spending on looks', 'Fun with friends', 'Punctuality']
    df1 = df1[mycolumns]
    punct   = pd.get_dummies(df1['Punctuality'])
    df1.drop(['Punctuality'], axis=1, inplace=True)
    df1 = df1.join([punct])
    #Instead of doing multi-label prediction, splitting predict avr into two groups - 
    df1.loc[df1['Finances'] <= 3, 'Finances'] = 0
    df1.loc[df1['Finances'] > 3, 'Finances'] = 1
    final_columns = ['Finances', 'Prioritising workload','Keeping promises', 'Decision making', 'Thinking ahead', 'Questionnaires or polls', 'Getting up', 'Entertainment spending', 'Spending on looks', 'Fun with friends', 'i am often running late']
    df2 = df1[final_columns]
    print df2.columns
    return df2

def modeling(df2):
    # Option using cross validation

    X = df2.drop(['Finances'], axis=1)
    y = df2['Finances']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    logreg_pipe = Pipeline([('logpred', LogisticRegression())])

    cv = model_selection.ShuffleSplit(n_splits=20, test_size=0.2, random_state=42)
    param_grid = { 'logpred__C':[.01,.03,.1,.3,1,3,10] }    # parameters to Pipeline take the form [label]__[estimator_param]
    logreg_cv = model_selection.GridSearchCV(logreg_pipe, param_grid=param_grid, cv=cv)  # cv=kf

    logreg_cv.fit(X_train, y_train)
    logreg_cv.predict(X_test)
    print "Score: ", logreg_cv.score(X_test, y_test)
    #cv_results = logreg_cv.cv_results_
    #print "results: " 
    print "best_score     : ", logreg_cv.best_score_
    #print "best_params    : ", logreg_cv.best_params_
    #print "best_estimator : ", logreg_cv.best_estimator_
    return logreg_cv

def predictor(mymodel, data):
    return mymodel.predict(data)

df2 = get_data()
mymodel = modeling(df2)
final_columns = ['Finances', 'Prioritising workload','Keeping promises', 'Decision making', 'Thinking ahead', 'Questionnaires or polls', 'Getting up', 'Entertainment spending', 'Spending on looks', 'Fun with friends', 'i am often running late']
test = pd.DataFrame(data = [[1.0, 5.0, 5.0, 5.0, 4.0, 3.0, 1.0, 2.0, 1.0, 2.0, 1.0]], columns=final_columns)
print test
X = test.drop(['Finances'], axis=1)
y = test['Finances']
pred = predictor(mymodel,X)
print "pred : ", pred
print "actual : ", y
print mymodel.predict_proba(X)