# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 11:13:12 2026

@author: hp
"""

import random

trials = 1000
count_sum_7 = 0

for _ in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    if die1 + die2 == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / trials
print(experimental_probability)