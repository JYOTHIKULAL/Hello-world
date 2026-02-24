# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 11:27:11 2026

@author: hp
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    'Transmission': ['Automatic', 'Manual', 'Manual', 'Automatic'],
    'Color': ['Red', 'Blue', 'Green', 'Blue']
}

df = pd.DataFrame(data)

le = LabelEncoder()
df['Transmission'] = le.fit_transform(df['Transmission'])

df = pd.get_dummies(df, columns=['Color'], drop_first=True)

print(df)