# -*- coding: utf-8 -*-
"""hw3_visualization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y9hjKh4DymqbgRB6_Xl3nYgt0VJo_6Ll

# Musicals! - Movie Analysis report by Max Kretschmer mtk739
Modify this cell by placing your name and eid in the space above.

## Homework 3

### Exploring the IMDb with Altair

Data, data everywhere, and not a insight to spare!  The internet movie database (IMDb) was one of the first really cool things to hit the internet in the 1990's.  If you are interested, read a little bit about this history of the website on its [wikipedia entry](https://en.wikipedia.org/wiki/IMDb).

Today, the data that powers the IMDb website is [available](https://www.imdb.com/interfaces/) for personal and non-commercial use. The file `imdb_musicals.csv` that comes with this assignment was made by fetching the data (Feb 2021), filtering out just the movies that included "Musical" as a genre, and merging that data with the average ratings and number of votes. I kept the column for `tconst (string) - alphanumeric unique identifier of the title`; it is named `uid` (a common name for the unique identifier, or database key).
"""

import altair as alt
import pandas as pd

# Read in the data
df = pd.read_csv('imdb_musicals.csv')

"""## Question 1 - Data Cleaning with list wise deletion

Each item in our table has the following attributes:
  - `uid` 
  - `title`
  - `year`
  - `runtime_mins`
  - `ave_rating`
  - `num_votes`
  
We want to visualize how this attributes interact with each other.  Some of these attributes are missing for some of the movies in our data set.  Perform "list wise deletion", aka, drop all the rows from the table that are missing any values. Use [dropna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html). Check your work by verifying there are $5306$ movies remaining in the dataframe
"""

# your code here
df_clean = df.dropna(axis=0)
df_clean

"""## Question 2 - What _is_ good?

Movies are rated on a 1-10 scale, but in our musical data set we want to understand what those distributions of the ratings look like.  

Use Altair to plot a histogram (using `mark_bar`) of the ratings with a ruler marker (using `mark_rule`) to denote the _median_ movie rating.  Use [this](https://altair-viz.github.io/gallery/histogram_with_a_global_mean_overlay.html) as a reference, and change the ruler mark to orange from red. 

Use 18 bins in your histogram.  

Set the x-axis label to "Average Rating" [doc](https://altair-viz.github.io/user_guide/customization.html#adjusting-axis-labels). 

Set the title of the plot to "Distribution of Musical Ratings". [doc](https://altair-viz.github.io/user_guide/configuration.html#config-title)

You might run into a small problem here ... Altair only allows 5,000 rows of a data set to be embedded in Chart.  Read about it in the [FAQ](https://altair-viz.github.io/user_guide/faq.html#disabling-maxrowserror) and use one of the suggested methods to get past the error. 
"""

# your code here
alt.data_transformers.disable_max_rows()

base = alt.Chart(df_clean)

bar = base.mark_bar().encode(
    x=alt.X('ave_rating:Q', bin=alt.Bin(maxbins=18), axis=alt.Axis(title="Average rating")),
    y='count()'
).properties(
    title='Distribution of Musical Ratings'
)

rule = base.mark_rule(color='orange').encode(
    x='median(ave_rating):Q',
    size=alt.value(5)
)

bar + rule

"""## Question 3 - Has our attention span changed? 

Plot the mean runtime of the musical as a function of year using `mark_line`. 

Have musicals gotten longer, shorter, or stayed the same?

Set the y-axis label to "Average Runtime" [doc](https://altair-viz.github.io/user_guide/customization.html#adjusting-axis-labels). 

Set the title of the plot to "Average Musical Runtimes Over the Years". [doc](https://altair-viz.github.io/user_guide/configuration.html#config-title)

The year on the x-axis should be formatted properly (this is the year 2021, not the year 2,021). The x-axis should start at the min of the year in the dataset. 
"""

# your code here
alt.Chart(df_clean).mark_line().encode(
    x = alt.X('year', axis=alt.Axis(format=".0f")),
    y = alt.Y('mean(runtime_mins)', axis=alt.Axis(title='Average Runtime'))
).properties(
    title='Average Musical Runtimes Over the Years'
)

"""## Question 4 - When were Musicals made?

Visualize the number of musicals made each year using an area chart with a gradiant using this [doc](https://altair-viz.github.io/gallery/area_chart_gradient.html) as a reference.

The y-axis should be labeled "Count of Musicals".

The graph should be titled "Number of Musicals Made by Year".

The year on the x-axis should be formatted properly.
"""

# your code here
alt.Chart(df_clean).mark_area(
    line={'color':'darkgreen'},
    color=alt.Gradient(
        gradient='linear',
        stops=[alt.GradientStop(color='white', offset=0),
               alt.GradientStop(color='darkgreen', offset=1)],
        x1=1, x2=1,
        y1=1, y2=0
    )
).encode(
    x = alt.X('year', axis=alt.Axis(format=".0f")),
    y = alt.Y('count()', axis=alt.Axis(title="Count of Musicals"))
).properties(
    title='Number of Musicals Made by Year'
)

"""## Question 5 - Explore the Musicals by Popularity

Create a scatter plot, where each dot is a musical.  

The position of the musical is encoded by year (x-axis), and average rating (y-axis). 

The size of the dot should encode the number of votes it received on IMDb.

The y-axis should be labeled "Average Rating".

The graph should be titled "Scatter plot of Musicals".

The year on the x-axis should be formatted properly.

Create an interactive tool tip that will display the title, runtime_mins, and num_votes for the movie when your mouse hovers over it, using the
[doc](https://altair-viz.github.io/gallery/scatter_tooltips.html) as an example. 
"""

# your code here
rangelim = lambda field: alt.Scale(domain=[df_clean[field].min(), df_clean[field].max()])

alt.Chart(df_clean).mark_point().encode(
    x = alt.X('year', axis=alt.Axis(format=".0f"), scale=rangelim('year')),
    y = alt.Y('ave_rating', axis=alt.Axis(title='Average Rating'), scale=rangelim('ave_rating')),
    size = alt.Size('num_votes', title='Number of Votes'),
    tooltip=['title', 'runtime_mins', 'num_votes', 'ave_rating']
).properties(
    title="Scatter plot of Musicals"
)