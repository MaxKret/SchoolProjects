# -*- coding: utf-8 -*-
"""Lab5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10H-HeeYNZKw6vbvNScrcPuDwHUnEWAXS
"""

# import the packages 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_excel('AidData.xlsx')

df

df['coalesced_purpose_code'].min()
df['coalesced_purpose_code'].max()

