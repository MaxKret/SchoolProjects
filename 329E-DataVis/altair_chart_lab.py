# -*- coding: utf-8 -*-
"""altair-chart-lab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mvfEBnKpVe4g-fzNiZgBTqxdnzUhxGDE

# Altair Simple Charts: Core Concepts Lab

## Group: 32

### Members: Max Kretschmer and Kabir Chadha

The goal of this lab is to teach you the core concepts required to create a basic Altair chart; namely:

- **Data**, **Marks**, and **Encodings**: the three core pieces of an Altair chart

- **Encoding Types**: ``Q`` (quantitative), ``N`` (nominal), ``O`` (ordinal), ``T`` (temporal), which drive the visual representation of the encodings

- **Binning and Aggregation**: which let you control aspects of the data representation within Altair.

With a good understanding of these core pieces, you will be well on your way to making a variety of charts in Altair.

We'll start by importing Altair:
"""

import altair as alt

"""## A Basic Altair Chart

The essential elements of an Altair chart are the **data**, the **mark**, and the **encoding**.

The format by which these are specified will look something like this:

```python
alt.Chart(data).mark_point().encode(
    encoding_1='column_1',
    encoding_2='column_2',
    # etc.
)
```

Let's take a look at these pieces, one at a time.

### The Data

Data in Altair is built around the [Pandas Dataframe](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html).
For this section, we'll use the cars dataset, which we can load using the [vega_datasets](https://github.com/altair-viz/vega_datasets) package:
"""

from vega_datasets import data
cars = data.cars()

cars.head()

"""Data in Altair is expected to be in a [tidy format](http://vita.had.co.nz/papers/tidy-data.html); in other words:

- each **row** is an observation
- each **column** is a variable

See  [Altair's Data Documentation](https://altair-viz.github.io/user_guide/data.html) for more information.

### The *Chart* object

With the data defined, you can instantiate Altair's fundamental object, the ``Chart``. Fundamentally, a ``Chart`` is an object which knows how to emit a JSON dictionary representing the data and visualization encodings, which can be sent to the notebook and rendered by the Vega-Lite JavaScript library.
Let's take a look at what this JSON representation looks like, using only the first row of the data:
"""

cars1 = cars.iloc[:1]
alt.Chart(cars1).mark_point().to_dict()

"""At this point the chart includes a JSON-formatted representation of the dataframe, what type of mark to use, along with some metadata that is included in every chart output.

### The Mark

We can decide what sort of *mark* we would like to use to represent our data.
In the previous example, we can choose the ``point`` mark to represent each data as a point on the plot:
"""

alt.Chart(cars).mark_point()

"""The result is a visualization with one point per row in the data, though it is not a particularly interesting: all the points are stacked right on top of each other!

It is useful to again examine the JSON output here:
"""

alt.Chart(cars1).mark_point().to_dict()

"""Notice that now in addition to the data, the specification includes information about the mark type.

There are a number of available marks that you can use; some of the more common are the following:

* ``mark_point()`` 
* ``mark_circle()``
* ``mark_square()``
* ``mark_line()``
* ``mark_area()``
* ``mark_bar()``
* ``mark_tick()``

You can get a complete list of ``mark_*`` methods using Jupyter's tab-completion feature: in any cell just type:

    alt.Chart.mark_
    
followed by the tab key to see the available options.

### Encodings

The next step is to add *visual encoding channels* (or *encodings* for short) to the chart. An encoding channel specifies how a given data column should be mapped onto the visual properties of the visualization.
Some of the more frequenty used visual encodings are listed here:

* ``x``: x-axis value
* ``y``: y-axis value
* ``color``: color of the mark
* ``opacity``: transparency/opacity of the mark
* ``shape``: shape of the mark
* ``size``: size of the mark
* ``row``: row within a grid of facet plots
* ``column``: column within a grid of facet plots

For a complete list of these encodings, see the [Encodings](https://altair-viz.github.io/user_guide/encoding.html) section of the documentation.

Visual encodings can be created with the `encode()` method of the `Chart` object. For example, we can start by mapping the `y` axis of the chart to the `Origin` column:
"""

alt.Chart(cars).mark_point().encode(
    y='Origin'
)

"""The result is a one-dimensional visualization representing the values taken on by `Origin`, with the points in each category on top of each other.
As above, we can view the JSON data generated for this visualization:
"""

alt.Chart(cars1).mark_point().encode(
    x='Origin'
).to_dict()

"""The result is the same as above with the addition of the `'encoding'` key, which specifies the visualization channel (`y`), the name of the field (`Origin`), and the type of the variable (`nominal`).
We'll discuss these data types in a moment.

The visualization can be made more interesting by adding another channel to the encoding: let's encode the `Miles_per_Gallon` as the `x` position:
"""

alt.Chart(cars).mark_point().encode(
    y='Origin',
    x='Miles_per_Gallon'
)

"""You can add as many encodings as you wish, with each encoding mapped to a column in the data.
For example, here we will color the points by *Origin*, and plot *Miles_per_gallon* vs *Year*:
"""

alt.Chart(cars).mark_point().encode(
    color='Origin',
    y='Miles_per_Gallon',
    x='Year'
)

"""---

## Encoding Types

One of the central ideas of Altair is that the library will **choose good defaults for your data type**.

The basic data types supported by Altair are as follows:

<table>
  <tr>
    <th>Data Type</th>
    <th>Code</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>quantitative</td>
    <td>Q</td>
    <td>Numerical quantity (real-valued)</td>
  </tr>
  <tr>
    <td>nominal</td>
    <td>N</td>
    <td>Name / Unordered categorical</td>
  </tr>
  <tr>
    <td>ordinal</td>
    <td>O</td>
    <td>Ordered categorial</td>
  </tr>
  <tr>
    <td>temporal</td>
    <td>T</td>
    <td>Date/time</td>
  </tr>
</table>

When you specify data as a pandas dataframe, these types are **automatically determined** by Altair.

When you specify data as a URL, you must **manually specify** data types for each of your columns.

Let's look at a simple plot containing three of the columns from the cars data:
"""

alt.Chart(cars).mark_tick().encode(
    x='Miles_per_Gallon',
    y='Origin',
    color='Cylinders'
)

"""Questions to ponder:

- what data type best goes with ``Miles_per_Gallon``?
- what data type best goes with ``Origin``?
- what data type best goes with ``Cylinders``?

Let's add the shorthands for each of these data types to our specification, using the one-letter codes above
(for example, change ``"Miles_per_Gallon"`` to ``"Miles_per_Gallon:Q"`` to explicitly specify that it is a quantitative type):
"""

alt.Chart(cars).mark_tick().encode(
    x='Miles_per_Gallon:Q',
    y='Origin:N',
    color='Cylinders:O'
)

"""Notice how if we change the data type for ``'Cylinders'`` to ordinal the plot changes.

As you use Altair, it is useful to get into the habit of always specifying these types explicitly, because this is *mandatory* when working with data loaded from a file or a URL.

### Lab Exercises

Create the following Graphs:

  1. A Scatter plot of "Weight_in_lbs" on the x-axis, and "Acceleration" in the y-axis with the number of cylinders encoded in the color channel of all the cars in the dataframe. 
  2. A horizontal histogram of the country of origin ([this documentation](https://altair-viz.github.io/gallery/simple_histogram.html) might help) of all the cars in the dataframe. 
  3. A Heatmap of the binned horsepower (x) and the binned displacement (y) with the count representing color. ([this documentation](https://altair-viz.github.io/gallery/binned_heatmap.html) might help).  Use 20 bins for each dimension.
"""

# Code for visualization 1
alt.Chart(cars).mark_point().encode(
    x="Weight_in_lbs",
    y="Acceleration",
    color="Cylinders:O"
)

# Code for visualization 2
alt.Chart(cars).mark_bar().encode(
    x='count():Q',
    y='Origin:O'
)

from altair.vegalite.v4.schema.core import Color
# Code for visualization 3
alt.Chart(cars).mark_rect().encode(
    alt.X('Horsepower:Q', bin = alt.Bin(maxbins=20)),
    alt.Y('Displacement:Q', bin = alt.Bin(maxbins=20)),
    alt.Color('count():Q', scale=alt.Scale(scheme='greenblue'))
)