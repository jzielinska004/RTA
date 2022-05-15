#!/usr/bin/env python
# coding: utf-8

# In[19]:


from sklearn import datasets
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle
import numpy as np
get_ipython().system('pip install flask_server')
from flask import Flask
from flask_server import Perceptron


iris = load_iris()
iris = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names']+['target'])

classifier = Perceptron(0.001, 1000)

X = iris.iloc[:, 0:2].values
Y = iris.iloc[:, 4].values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

X_train = X_train.astype(float)
Y_train = Y_train.astype(float)

classifier.fit(X_train, Y_train)

with open('model.pkl', 'wb') as moj_model:
    pickle.dump(classifier, moj_model)

