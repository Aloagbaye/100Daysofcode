# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 22:49:17 2022

@author: alomo
"""

import numpy as np
import pandas as pd

from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv("iris.csv")

X = data.drop(['variety'],axis=1)
y = data['variety']

X_train, X_test, y_train, y_test = train_test_split(X,y)

model = LogisticRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print(metrics.accuracy_score(y_test,y_pred))
model.predict(np.array([[2.5,1.2,3.4,4.8]]))