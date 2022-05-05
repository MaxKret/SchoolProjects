# -*- coding: utf-8 -*-
"""Python Pandas and Matplotlib Group Lab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zLvRGTnIzrUqqZ5Cv0UT_zf7WJbBD-Wo

# Group Lab Activity

### Group number: 

### Members of the group: (fill this in!!!)
  - Max K
"""

# import the packages 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

"""## Step one - Series

First, we want to create a `pandas` `Series` object that has length 3 and the first element is `nan` 
"""

s = pd.Series([np.nan,12.03, 43.1])

s

"""### Do a numerical operation on the Series

Multiply the series by the scalar 0.5
"""

s*0.5

"""### Store the result in another series object

The result of the last operation wasn't stored in a variable, assign the operation to a variable called `s1`
"""

s1 = s*0.5

s1

# We can also add these two series! 
s + s1

"""## Creating DataFrames"""

# by using a multiple series
df = pd.DataFrame( {'a':s,'b':s1})

df

# by using a dict
d = {'a':[1,2,3],
     'b':[9,5,2]}

df = pd.DataFrame(d)

df

# Commented out IPython magic to ensure Python compatibility.
# checkout whats in memory right now just for fun
# %whos

# now, let's load from a file
df = pd.read_csv('titanic.csv')

"""## Investigate the DataFrame

Now the titanic data is loaded into the variable `df`, what can we learn about it?
"""

# The first 5 rows
df.head(5)

# the last 5 rows
df.tail(5)

# the column names and their types
df.dtypes

# the length of the dataframe
len(df)

"""## Slicing and Dicing

How to select rows and columns 
"""

# Select the 523 row (note ... the result is a Series with the indices represted by column names)
df.iloc[523]

foo = df.iloc[523]

# you can index the series using the classic dictionary-like syntax
foo['Name']

# Select all the rows where the flag survived = 1
df_survivors = df[ df['Survived'] == 1 ]

df_survivors.head()

# Select all the rows where the flag survived = 1 AND the Sex is male
df_survivors_men = df[ (df['Survived'] == 1) & (df['Sex'] == 'male') ]

df_survivors_men.head()

# Just show the Name and Fare columns 
df_survivors_men[['Name','Fare']]

# I want all of the male survivors from class 2 or three
class_23 = df_survivors_men[df_survivors_men["Pclass"].isin([2, 3])]

class_23.head()

# I want to remove the records from class_23 that have the Age set as nan
age_no_na = class_23[class_23["Age"].notna()]

age_no_na.head(5)

"""## Groupby and Pivot Tables

Panda's DataFrame also allows for you to analyze data using a "groupby" function, which combines split, apply, and combine functions.  See the [O'Reilly Python for Data Science](https://jakevdp.github.io/PythonDataScienceHandbook/03.08-aggregation-and-grouping.html#GroupBy:-Split,-Apply,-Combine) book for a great explanation. 

Pivot tables are multidimensional groupbys!  Read more [here](https://jakevdp.github.io/PythonDataScienceHandbook/03.09-pivot-tables.html)
"""

# Group the original dataframe by survival, then sum the values in each partition 
df.groupby('Survived').sum()

# That was great, but the sum of the column values doesn't really make any sense!
# What about finding the mean?
df.groupby('Survived').mean()

# Averaging every column doesn't make sense, just pick out the Fare column
df.groupby('Survived')['Fare'].mean()

# Now use groupby differently to determine the survival rate by sex
df.groupby('Sex')['Survived'].mean()

# Pivot tables ... this was all great, but what if I want to find the 
# survival rate by sex AND by cabin class?  We use pivot tables:
df.pivot_table('Survived', index='Sex', columns='Pclass')

"""## Visualization with Matplotlib

Let's make our very first (aww ❤️) information visualiztion!  How about a bar chart visualizing the
survival rate we just by sex and passenger class with matplotlib's bar function.  Note we add 
labels, and rotate the xticks to be more readable. 
"""

df_sex_class_survival = df.pivot_table('Survived', index='Sex', columns='Pclass')
ax = df_sex_class_survival.T.plot(kind='bar')
plt.ylabel('Survival Rate')
plt.title('Survial Rate By Class and Sex')
plt.xlabel('Passenger Class')
plt.xticks(rotation=0)

"""### On your own now! 

Answer the next four questions as a group, and have one member of your group turn in this file (ipynb) as today's lab.  You will be graded for correctness, not just completion.

## Q1 - What was the mean age of the male passengers in Pclass 1?
"""

df_pclass1_men = df[ (df['Pclass'] == 1) & (df['Sex'] == 'male') ]
mean_age = df_pclass1_men['Age'].mean()
mean_age

"""## Q2 - What was the mean Fare by Pclass?"""

out = df.groupby('Pclass')['Fare'].mean()
out

"""## Q3 - How many females under the age of 13 were there?"""

female_13 = df[ (df['Age'] < 13) & (df['Sex'] == 'female') ]
out = len(female_13)
out

"""## Q4 - Plot a histogram of the ages of all the passengers
Note - this is easier than the example above. See the documentation [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.hist.html). Use 20 equally spaced bins. You can control the plot with matplotlib's functions, like `grid`, `xlabel`, `ylabel`, and `title`

You are expected to label, use readable fonts, and do not plot grid lines. 
"""

df['Age'].plot.hist(bins=20)
plt.ylabel('Number of Passengers')
plt.title('Passenger Ages')
plt.xlabel('Age')
plt.grid(visible=False)