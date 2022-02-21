import plotly.figure_factory as ff
import pandas as pd
import csv

ds = pd.read_csv("data.csv")
fig = ff.create_distplot([ds["Avg Rating"].tolist()],["Avg Rating"],show_hist = False)
fig.show()
