# -*- coding: utf-8 -*-
"""Implementation_Final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tMSxZMqJ9EcoOwuiOcuvmioUwBfcqEcA

# Final Implementation 

## Extract Fetal ECG - Final Project 29 

### Kabir Chadha, Maxwell Kretschmer, Jack Rickman

#Load Data Into Colab
##__WARNING__! First:
Upload the 5 .zip files from the provided 'Data Set' folder into colab and make sure to wait for them to finish before running the below cell. The '!unzip' commands can then be commented out again in case of a need to restart and run all.
"""

# # DATA UNPACKING
# # Load in the data, then uncomment and run:
# !unzip "/content/set-a-text.zip"
# !unzip "/content/set-a-text-test.zip"
# !unzip "/content/set-a-ext-text.zip"
# !unzip "/content/set-a-ext-text-test.zip"
# !unzip "/content/edf_files.zip"

"""##Imports"""

import pandas as pd
import altair as alt
import numpy as np

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# !pip install pyedflib
# import pyedflib
# from pyedflib import highlevel

"""#First Visualization Setup and Vis"""

# DATA LOADING AND CLEANING
all_records = []

number_of_files = 9

for i in range(1, number_of_files+1):
    df = pd.read_csv("a0{}.csv".format(i), skiprows=[1])
    df.rename(columns={"\'Elapsed time\'": "elapsedTime", "\'AECG1\'": "AECG1", "\'AECG2\'": "AECG2", "\'AECG3\'": "AECG3", "\'AECG4\'":"AECG4"}, inplace=True)
    all_records.append(df)

number_of_files = 76

for i in range(10, number_of_files):
    df = pd.read_csv("a{}.csv".format(i), skiprows=[1])
    df.rename(columns={"\'Elapsed time\'": "elapsedTime", "\'AECG1\'": "AECG1", "\'AECG2\'": "AECG2", "\'AECG3\'": "AECG3", "\'AECG4\'":"AECG4"}, inplace=True)
    all_records.append(df)

alt.data_transformers.disable_max_rows()

x = 58 # a59
sliced = all_records[x][:30000] # first 30s only
sliced_long =  pd.melt(sliced, ['elapsedTime'])

sliced_long.rename(columns = {'variable':'channel', 'value':'ECG'}, inplace = True)

make = pd.DataFrame({'channel': list(sliced_long['channel'].unique())})

my_multi_selection = alt.selection_multi(fields=['channel'], name="channelselect")
channel_scale = alt.Scale(domain=list(sliced_long['channel'].unique()),
                         range=['#FF0000', '#00FF00', '#0099ff', '#4800ff'])

interval = alt.selection_interval(encodings=['x'], name="intervalselect")

color_condition = alt.condition(my_multi_selection, alt.Color('channel:N', scale=channel_scale), alt.value('lightgray'), legend=None)

show_channel_selector = alt.Chart(make).mark_rect().encode(
    y='channel', color=color_condition
).add_selection(my_multi_selection)

base = alt.Chart(sliced_long).mark_line().encode(
    x=alt.X('elapsedTime:Q', title="Time Elapsed (second)"),
    y=alt.Y('ECG:Q', title="ECG Value", scale=alt.Scale(domain=[min(list(sliced_long['ECG'].unique()))-10, max(list(sliced_long['ECG'].unique()))+10])),
    tooltip=['ECG'],
    color=alt.Color('channel:N', scale=channel_scale, title="ECG Channel")
).add_selection(
    my_multi_selection
).transform_filter(
    my_multi_selection
).properties(
    width=2000
)

FullExtent = base.add_selection(
    interval
).properties(
    height=200
)

ZoomedExtent = base.encode(
    x=alt.X('elapsedTime:Q', scale=alt.Scale(domain=interval.ref()), title="Time Elapsed (second)")
).properties(
    height=500,
    title="Zoom and Channel Selection"
)


main_vis = ZoomedExtent & FullExtent
final = main_vis & show_channel_selector
final

# SAVE CHART AS HTML
# final.save('Final_Vis1.html')

"""#Second Visualization Setup and Vis"""

signals1, signal1_headers1, header1 = highlevel.read_edf('r01.edf')
signals4, signal_headers4, header4 = highlevel.read_edf('r04.edf')
signals7, signal_headers7, header7 = highlevel.read_edf('r07.edf')
signals8, signal_headers8, header8 = highlevel.read_edf('r08.edf')
signals10, signal_headers10, header10 = highlevel.read_edf('r10.edf')

def columnRpeak(df, peaks):
  print("Amount of fetal R peaks:", len(peaks))
  print('Average fetal beat per minute:', len(peaks)/5)
  df['fetal R peaks'] = 0
  for i in range(len(peaks)):
    index = (peaks[i]*1000)
    df.at[index,'fetal R peaks']=1
  return df

def intervalBPM(rpeaks):
  start = 0
  end = 7
  all_bpm = []
  all_peaks = []
  peaks = []
  for i in range(len(rpeaks)):
    if  rpeaks[i] >= start and rpeaks[i] <= end:
      peaks.append(rpeaks[i])
    else:
      bpm = round(len(peaks) * 60 / 7)
      all_bpm.append(bpm)
      all_peaks.append(peaks)
      if bpm < 110 or bpm > 160:
        print(peaks)
        print(bpm)
      peaks = []
      start += 7
      end += 7
      peaks.append(rpeaks[i])
  return all_bpm

peaks1 = [row[0] for row in header1['annotations']] # Timestamps of fetal R peaks
r01 = pd.DataFrame({
    "direct":signals1[0],
    "ch1":signals1[1],
    "ch2":signals1[2],
    "ch3":signals1[3],
    "ch4":signals1[4],
})

r01 = columnRpeak(r01, peaks1)

peaks4 = [row[0] for row in header4['annotations']]
r04 = pd.DataFrame({
    "direct":signals4[0],
    "ch1":signals4[1],
    "ch2":signals4[2],
    "ch3":signals4[3],
    "ch4":signals4[4]
})
r04 = columnRpeak(r04, peaks4)

peaks7 = [row[0] for row in header7['annotations']] 
r07 = pd.DataFrame({
    "direct":signals7[0],
    "ch1":signals7[1],
    "ch2":signals7[2],
    "ch3":signals7[3],
    "ch4":signals7[4]
})
r07 = columnRpeak(r07, peaks7)

peaks8 = [row[0] for row in header8['annotations']] 
r08 = pd.DataFrame({
    "direct":signals8[0],
    "ch1":signals8[1],
    "ch2":signals8[2],
    "ch3":signals8[3],
    "ch4":signals8[4]
})
r08 = columnRpeak(r08, peaks8)

peaks10 = [row[0] for row in header10['annotations']]
r10 = pd.DataFrame({
    "direct":signals10[0],
    "ch1":signals10[1],
    "ch2":signals10[2],
    "ch3":signals10[3],
    "ch4":signals10[4]
})
r10 = columnRpeak(r10, peaks10)

bpm1 = intervalBPM(peaks1)
bpm4 = intervalBPM(peaks4)
bpm7 = intervalBPM(peaks7)
bpm8 = intervalBPM(peaks8)
bpm10 = intervalBPM(peaks10)

# # Generating Data
# t = np.arange(1,42,1)
# source = pd.DataFrame({
#     'r01': bpm1,
#     # 'r04': bpm4,
#     # 'r07': bpm7,
#     # 'r08': bpm8
#     # 'r10': bpm10
# })
# df_long = source.melt(var_name="Mother", value_name="BPM")
# alt.Chart(df_long).mark_area(
#     opacity=0.5,
#     interpolate='step'
# ).encode(
#     alt.X('BPM:Q', bin=alt.Bin(maxbins=100)),
#     alt.Y('count()', stack=None),
#     alt.Color('Mother:N')
# ).properties(
#     title='Overlapping Histograms',
#     width=600,
#     height=400
# )

time_labels = [str(x)+"-"+str(x+7) for x in range(0,294,7)]
ymax = np.zeros(42) + 170
ymin = np.zeros(42) + 110
perc_diff = np.diff(bpm1, prepend=bpm1[0])
bpmG = pd.DataFrame({
    'BPM': bpm1,
    'Time Interval':time_labels,
    'ymax':ymax,
    'ymin':ymin,
    'Percent Change':perc_diff
})

    
base = alt.Chart(bpmG, title="Fetal Heart Beat Rate Over Time")

line = base.mark_line().encode(
    y=alt.Y('BPM:Q', scale=alt.Scale(domain= [ min(list(bpmG['BPM'].unique()))-15, max(list(bpmG['BPM'].unique()))+25 ] ), title='Beats Per Minute'),
    x=alt.X('Time Interval:O', sort=None, title='Time Interval (seconds)')
)

pt = base.mark_point(filled=True, size=80).encode(
    y=alt.Y('BPM:Q', scale=alt.Scale(domain= [ min(list(bpmG['BPM'].unique()))-15, max(list(bpmG['BPM'].unique()))+25 ] )),
    x=alt.X('Time Interval:O', sort=None),
    tooltip=['BPM','Percent Change'],
    color=alt.Color('Percent Change:Q', scale=alt.Scale(scheme='redblue')),
    size=alt.Size()
)
rule1 = base.mark_rule(color="rgb(255,1,1)").encode(
    y='ymax:Q'
)
rule2 = base.mark_rule(color="rgb(255,1,1)").encode(
    y='ymin:Q'
)
line + pt + rule1 + rule2