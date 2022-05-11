# -*- coding: utf-8 -*-
"""hw2_visualization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_iBjOTGQuWARog6u8SAzwDOjMZNoDq4r

# UFO report by mtk739
Modify this cell by placing your eid in the space above.

## Homework 1
You are a UFO researcher and have just obtained some **TOP SECRET** government data. The data contain sighting information including location, shape and source of the information. Use your pandas skills to investigate the data. Turn in this notebook as your report. Follow the directions and answer the questions. Edit the code cells to create pandas and matplotlib solutions to the questions. The first cell loads the data into a data frame called `df_sightings`. The rest is up to you.

The truth is out there...
"""

# this cell loads the ufo data (the file should be in the same directory as this notebook)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#
filename = 'ufo_location_shape.csv'
df_sightings = pd.read_csv(filename)
df_sightings.head()

"""## Data Exploration

Answer the following questions about the data in the csv file.  Your answer should be readable, and the only number in the output for the cell.

<p>How large is the data? How many rows and columns are there? What are the column names or keys?Use the cell below to create python code that prints the answer to the question</p>
This question is worth 1 pt.

### Question 1

How many sightings are in the `df_sightings`?
"""

# your code here
len(df_sightings)

"""### Question 2 

How many columns are there in the `df_sightings`? 
"""

# your code here
len(df_sightings.dtypes)

"""### Question 3

What are the column names?  Format the output such that there is one column name per line.
"""

# your code here
for col in df_sightings.columns:
  print(col)

"""### Question 4

List the unique countries where sightings occurred. Format the output such that there is one country name  per line. Only list valid countries (invalid country names will be easy to spot). 

You will notice our old friend from the tutorial pop up, `nan`.  By default when you read in a csv file, any of the following values in cells are filled with the numpy `nan` value:  ‘’, ‘#N/A’, ‘#N/A N/A’, ‘#NA’, ‘-1.#IND’, ‘-1.#QNAN’, ‘-NaN’, ‘-nan’, ‘1.#IND’, ‘1.#QNAN’, ‘<NA>’, ‘N/A’, ‘NA’, ‘NULL’, ‘NaN’, ‘n/a’, ‘nan’, ‘null’.
    
You can drop `nan` from a series using the `dropna` [method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dropna.html). 
    
Use the iterator [iteritems](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.iteritems.html) to loop through a series. Use the function [drop_duplicates](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.drop_duplicates.html) to remove duplicates from a series. 

"""

# your code here
countries = df_sightings['Country'].drop_duplicates().dropna()
for (i,c) in countries.iteritems():
  print(c)

"""### Question 5

For only sightings that occurred in the USA, list the unique state names. Format the output such that there is one US State name per line.
"""

# your code here
states = df_sightings[df_sightings['Country'] == 'USA ']['State'].drop_duplicates()
out = states.mask(states.eq('?? ')).dropna()
for (i,s) in out.iteritems():
  print(s)

"""### Question 6

List the different observed UFO shapes and the number of times that they occur in the data frame (hint see [value_counts](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html). The answer will be in text format with one type of shape followed by the number of occurances per line. 
"""

# your code here
Shapes_sightings = df_sightings['Shape']
Shapes_freq = Shapes_sightings.value_counts()
for (i,s) in Shapes_freq.iteritems():
  print(i,s)

"""### Question 7

Create a bar chart showing the number of sightings in each country. The x axis should be country and the y axis should be number of sightings.
        
Your axis should be legible, and labeled correctly.

Sort the countries by most sightings, to least sightings.  For the top three countries, annotate the bar chart to show the number of sightings, and adjust the y limits such that you are only showing the detail from 0-16 sightings. 

There are multiple ways to solve this, and I used [figure](https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.figure.html) to adjust the size of my plot, [ylim](https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.ylim.html) to control the y limits of the histogram, [value_counts](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html) to create the data, [bar](https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.bar.html) to chart the data, [xticks](https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks) to set the tick labels, [arrange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html) to create x coordinates for the countries and control the tick locations, [text](https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.text.html) to annotate the graph for the top three country sighting counts, and [ylabel](https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.ylabel.html) [title](https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.title.html) to set the ylabel and title of the plot.  
"""

# your code here
countries = df_sightings['Country']

plt.figure(figsize=(14,4))
plt.ylim(0,16)
freq_series = countries.value_counts().rename( {"The Bahamas (Bermuda triangle) ": "The Bahamas "} )
freq_series.plot.bar(x='Country')
plt.xticks(rotation=80)
plt.text(-0.25,16.25,str(freq_series.iloc[0]), rotation=40)
plt.text(0.75,16.25,str(freq_series.iloc[1]), rotation=40)
plt.text(1.75,16.25,str(freq_series.iloc[2]), rotation=40)
plt.xlabel("Country")
plt.ylabel("# of Sightings")
plt.title("UFO Sightings by Country")

"""### Question 8

Create a stacked bar chart showing the top 7 UFO shapes for the ten states with the highest number of sightings. Start by finding the ten states with the highest number of sightings. Given those 10 states, find the top 7 most frequent UFO shapes. Then for each state plot a stacked bar where each color of the stack corresponds to the number of sightings in that state for a particular UFO shape. Label the x-axis with the State abbreviation. 

There is an [example](https://matplotlib.org/3.2.2/gallery/lines_bars_and_markers/bar_stacked.html) of a stacked bar chart available in the documentation. 

Use the color brewer website from the class slides to pick 7 colors to override the matplotlib defaults for the bars.
"""

# your code here (feel free to make more cells if it makes things easier for you ... the problem has multiple steps)

Shapes = Shapes_freq.keys().tolist()
num_total_shapes = len(Shapes)
z = df_sightings[['State', 'Shape']]
top_states_freq = z['State'].value_counts().head(10)
top_states = top_states_freq.keys().tolist()
shape_freqs_by_state = [z[z['State'] == top_states[i]].value_counts(subset=['Shape']) for i in range(10)]
y = dict(zip([top_states[i] for i in range(10)], shape_freqs_by_state))

unzip_keys = lambda a: [x[0] for x in a.keys().tolist()]

pp = y.copy()
def fill_shapes(x):
  v = []
  for shp in Shapes:
    if shp not in [i[0] for i in x.keys().tolist()]:
      v.append(shp)
  newseries = pd.Series([0]*len(v), index=v)
  x.index = unzip_keys(x)
  return pd.concat([x,newseries])
  

msk = [False]*7 + [True]*14
for key in y:
  y[key] = fill_shapes(y[key])
  y[key] = y[key].mask(cond=msk,other=0)
  
# # What I NEED # #
# {'CA ' : series['Lights Only '        92, 'Fireball '        50, 'Circle '         35], 'FL ' : ['Lights Only '        92, 'Fireball '        50, 'Circle '         35]}
# 
# # 
# shape_freqs = {'Lights Only ': [92,...], 'Fireball ':[50,...], 'Circle ':[35,...]}
# #
# lights_bar = shape_freqs['Lights Only ']
# 
shape_freqs = {shp: [] for shp in Shapes}
for key in y:
  for (key,value) in y[key].items():
    shape_freqs[key].append(value)

fig, ax = plt.subplots()
plt.figure(figsize=(15,10))
width = 0.35       # the width of the bars: can also be len(x) sequence

shp_reverse = Shapes.copy()
shp_reverse.reverse()

colors = ['#cab2d6','#a6cee3','#1f78b4','#b2df8a','#33a02c','#fb9a99','#e31a1c','#fdbf6f','#ff7f00']
c_curr = ''
c_idx = 0

legend_labels = []
bottom = np.zeros(shape=(10,))
curr_bar = np.ndarray(shape=(10,))
for key in shp_reverse:

  if shape_freqs[key] == [0]*10:
    legend_labels.append('_'+key)
  else:
    legend_labels.append(key)
    c_curr = colors[c_idx]
    c_idx += 1


  if key == 'Missile/Rocket ':
    #First Run
    curr_bar = shape_freqs[key]
    ax.bar(top_states, curr_bar, width, label=key, color=c_curr)
    bottom = bottom + curr_bar
  else:
    #Normal Procedure
    curr_bar = shape_freqs[key]
    ax.bar(top_states, curr_bar, width, bottom=bottom, label=key, color=c_curr)
    bottom = bottom + curr_bar

ax.set_ylabel('Sightings')
ax.set_title('Top 7 UFO Shapes in the Top 10 States')
handles, _ = ax.get_legend_handles_labels()
ax.legend(handles=handles, labels=legend_labels, fontsize=8)

for state in top_states:
  total = y[state].sum()
  ax.text(state, y[state].sum()+2.5, str(total), ha='center')

plt.show()