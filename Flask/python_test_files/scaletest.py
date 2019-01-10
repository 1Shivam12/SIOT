# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:02:14 2019

@author: Shivam Bhatnagar
"""
from sklearn import preprocessing
import numpy as np

imdblist = [7.2,7.5,7.3,8.7,7.7,7.4]

imlist = np.array(imdblist)

imlist = preprocessing.scale(imlist)

print(imdblist)
print(imlist)

