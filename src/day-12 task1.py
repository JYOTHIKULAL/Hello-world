# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 11:28:17 2026

@author: hp
"""

import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 65, 70, 75, 85, 90, 95]

plt.scatter(study_hours, scores, marker='o')

plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.title("Study Hours vs Exam Scores")

plt.grid(True)

plt.show()