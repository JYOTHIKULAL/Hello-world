# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 12:15:19 2026

@author: hp
"""

import pandas as pd

df = pd.read_csv("location_dirty_data.csv")

print(df["Location"].unique())

df["Location"] = df["Location"].str.title()   # or use .str.lower()

print(df["Location"].unique())