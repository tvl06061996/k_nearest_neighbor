# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:29:28 2019

@author: loc.tran
"""
import operator
import numpy as np
from collections import Counter


class NearestNeighbors():
    def __init__(self, k = 3):
        self.k = k
        
    def fit(self, train, label, test):
        distances = {}
        for i, x in enumerate(train):
            distances[i] = np.linalg.norm(x - test)
        
        sort = sorted(distances.items(), key=operator.itemgetter(1))
        neighbors = []
        for i in range(self.k):
            neighbors.append(sort[i][0])
        result = Counter(neighbors).most_common(1)[0][0]
        return label[result]
            
        