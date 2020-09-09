import plotly
import plotly.express as px
import pandas as pd

xlWorkbook = "Sample.xlsx"
df = pd.read_excel(xlWorkbook)
fig = px.bar(df, x=df['API Name'], y=[df['Total TC passed'],df['Total TC Failed']], title="Test Case Summary",labels={'value':'Test Cases Count'} , barmode='stack')
fig.show()

plotly.offline.plot(fig, filename="TestCaseReport.html")
