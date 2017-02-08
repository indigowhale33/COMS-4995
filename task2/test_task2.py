from __future__ import print_function, division
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
#from sklearn.cross_validation import cross_val_score
from sklearn.neighbors import KNeighborsClassifier as KNN

#import pytest

def division(x,y):
	return x/y

def test_div():
	assert division(2,8) == 0.25

def test_np_div():
	two = np.array([2])
	eight = np.array([8])
	assert division(two,eight) == 0.25

def test_input():
	with open('../input.txt', 'rb') as f:
		assert len(f.read().decode('utf-8')) == 7

def test_KNN():
	iris = load_iris()
	X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=42)
	knn = KNN(5)
	scores = cross_val_score(knn, X_test, y_test, cv=5, scoring='accuracy')
	assert scores.mean() > 0.7
