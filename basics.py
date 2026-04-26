# Importing Libraries
# pip install pandas numpy matplotlib seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Loading Data
df = pd.read_csv('pokemon_complete.csv')
# for excel files do: df = pd.read_excel('pokemon_complete.xlsx')
df.head() # shows the first five rows
