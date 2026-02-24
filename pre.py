# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 10:18:33 2026

@author: hp
"""

import matplotlib.pyplot as plt

# Sample data
days = [1, 2, 3, 4, 5]
temperature = [30, 32, 31, 35, 36]

# Create line plot
plt.plot(days, temperature)
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.title("Daily Temperature Trend")

# Show plot
plt.show()
