import pandas as panda
import plotly.express as plot

df = panda.read_csv("CopyData.csv")

lineGraph = plot.line(df,x="date",y="cases",color="country",title="Covid Cases for each Country")
lineGraph.show()

sc = panda.read_csv("Copy+of+data+-+data.csv")

scatterChart = plot.scatter(df,x="date",y="cases",color="country",title="Covid Casesfor each Country",size_max=80)
scatterChart.show()