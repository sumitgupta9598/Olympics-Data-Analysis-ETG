# -*- coding: utf-8 -*-
"""Olympics Data Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-HrJ2EKVAvDEvXq1kxytntZBZ3ItFQRL
"""

import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("summer.csv")

df.head()

df.isnull().sum()

"""
**1. In how many cities Summer Olympics is held so far?**"""

len(df['City'].unique())

"""**2. Which sport is having most number of Gold Medals so far? (Top 5)**"""

df_gold = df[df['Medal'] == 'Gold']
df_gold.groupby('Sport').count()['Medal'].sort_values(ascending = False).head().plot.bar(figsize=(10,5))

"""**3. Which sport is having most number of medals so far? (Top 5)**"""

data=[]
for Medal in df['Sport'].unique():
 data.append([Medal,len(df[df['Sport']==Medal])])
data=pd.DataFrame(data,columns=['sports','Medals'])
data.sort_values(by='Medals',ascending=False).head().plot.bar(figsize=(16,8))
data.sort_values(by='Medals',ascending=False).head()

"""**4. Which player has won most number of medals? (Top 5)**"""

df.groupby('Athlete').count()['Medal'].sort_values(ascending = False).head().plot.bar(figsize=(16,8))

"""**5. Which player has won most number Gold Medals of medals? (Top 5)**"""

df_gold = df[df['Medal'] == 'Gold']
df_gold.groupby('Athlete').count()['Medal'].sort_values(ascending = False).head().plot.bar(figsize=(16,8))

"""**6. In which year India won first Gold Medal in Summer Olympics?**"""

df_india = df[df['Country'] == 'IND']
df_gold = df_india[df_india['Medal'] == 'Gold']
df_gold.groupby('Year').count()['Medal'].head(1)

"""**7. Which event is most popular in terms on number of players? (Top 5)**"""

df.groupby('Event').count()['Athlete'].sort_values(ascending = False).head().plot.bar(figsize=(16,8))

"""**8. Which sport is having most female Gold Medalists? (Top 5)**"""

df_women = df[df['Gender'] == 'Women']
df_gold = df_women[df_women['Medal'] == 'Gold']
 
df_gold.groupby('Sport').count()['Medal'].sort_values(ascending = False).head().plot.bar(figsize=(16,8))