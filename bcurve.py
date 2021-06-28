import plotly.figure_factory as ff
import csv
import pandas as pd

df = pd.read_csv("Bcurve_data.csv")
fig = ff.create_distplot([df["Avg Rating"].to_list()],["Average Rating"])
fig.show()