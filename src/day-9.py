# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 14:33:37 2026

@author: hp
"""

import pandas as pd
s1=pd.Series([10,20,30,40])
s2=pd.Series([10,20,30],index=['a','b','c'])
print(s1)
print(s2)


marks=pd.Series([85,90,78],index=['maths','pysics','chemistry'])
print(marks['maths'])
print(marks[['maths','chemistry']])

#boolean masking
scores=pd.Series([45,67,89,34,90])

passed=scores[scores>60]
print(passed)

#handling missing data
data=pd.Series([10,None,30,None])
print(data.isnull())
print(data.fillna(2))

#vectorized string
names=pd.Series(['alice','bob','JYOTHI'])
print(names.str.lower())
print(names.str.contains('a'))