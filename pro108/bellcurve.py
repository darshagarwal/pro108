import pandas as pd
import plotly.figure_factory as ff

df= pd.read_csv("pro108/data.csv")
Brand_list=df["Mobile Brand"].tolist()
rating_list=df["Avg Rating"].tolist()
fig=ff.create_distplot([rating_list],["Weight"],show_hist=False)
fig.show()