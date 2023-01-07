import pandas as pd
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_white"


control_data = pd.read_csv("control_group.csv", sep=";")
test_data = pd.read_csv("test_group.csv", sep=";")
control_data.columns = ["Campaign Name", "Date", "Amount Spent", "Number of Impressions",
                        "Reach", "Website Clicks", "Searches Received", "Content Viewed",
                        "Added to Cart", "Purchases"]
test_data.columns = ["Campaign Name", "Date", "Amount Spent", "Number of Impressions",
                     "Reach", "Website Clicks", "Searches Received", "Content Viewed",
                     "Added to Cart", "Purchases"]
control_data["Number of Impressions"].fillna(value=control_data["Number of Impressions"].mean(), inplace=True)
control_data["Reach"].fillna(value=control_data["Reach"].mean(), inplace=True)
control_data["Website Clicks"].fillna(value=control_data["Website Clicks"].mean(), inplace=True)
control_data["Searches Received"].fillna(value=control_data["Searches Received"].mean(), inplace=True)
control_data["Content Viewed"].fillna(value=control_data["Content Viewed"].mean(), inplace=True)
control_data["Added to Cart"].fillna(value=control_data["Added to Cart"].mean(), inplace=True)
control_data["Purchases"].fillna(value=control_data["Purchases"].mean(), inplace=True)

ab_data = control_data.merge(test_data, how="outer").sort_values(["Date"])
ab_data = ab_data.reset_index(drop=True)

# figure = px.scatter(data_frame=ab_data,
#                     x='Number of Impressions',
#                     y='Amount Spent',
#                     size="Amount Spent",
#                     color="Campaign Name",
#                     trendline="ols")
# figure.show()

# label = ["Total Searches from Control Campaign",
#          "Total Searches from Test Campaign"]
# counts = [sum(control_data["Searches Received"]),
#           sum(test_data["Searches Received"])]
# colors = ['gold', 'lightgreen']
# fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
# fig.update_layout(title_text='Control Vs Test: Searches')
# fig.update_traces(hoverinfo = 'label+percent', textinfo='value', textfont_size=30,
#                   marker=dict(colors=colors,
#                               line=dict(color='black', width=3)))
# fig.show()

# label = ["Website Clicks from Control Campaign",
#          "Website Clicks from Test Campaign"]
# counts = [sum(control_data["Website Clicks"]),
#           sum(test_data["Website Clicks"])]
# colors = ['gold', 'lightgreen']
# fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
# fig.update_layout(title_text='Control Vs Test: Website Clicks')
# fig.update_traces(hoverinfo='label+percent', textinfo='value',
#                   textfont_size=30,
#                   marker=dict(colors=colors,
#                               line=dict(color='black', width=3)))
# fig.show()

# label = ["Content Viewed from Control Campaign",
#          "Content Viewed from Test Campaign"]
# counts = [sum(control_data["Content Viewed"]),
#           sum(test_data["Content Viewed"])]
# colors = ['gold', 'lightgreen']
# fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
# fig.update_layout(title_text='Control Vs Test: Content Viewed')
# fig.update_traces(hoverinfo='label+percent', textinfo='value',
#                   textfont_size=30,
#                   marker=dict(colors=colors,
#                               line=dict(color='black', width=3)))
# fig.show()

# label = ["Added to Cart from Control Campaign",
#          "Added to Cart from Test Campaign"]
# counts = [sum(control_data["Added to Cart"]),
#           sum(test_data["Added to Cart"])]
# colors = ['gold', 'lightgreen']
# fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
# fig.update_layout(title_text='Control Vs Test: Added to Cart')
# fig.update_traces(hoverinfo='label+percent', textinfo='value',
#                   textfont_size=30,
#                   marker=dict(colors=colors,
#                               line=dict(color='black', width=3)))
# fig.show()

label = ["Amount Spent in Control Campaign",
         "Amount Spent in Test Campaign"]
counts = [sum(control_data["Amount Spent"]),
          sum(test_data["Amount Spent"])]
colors = ['gold', 'lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Control Vs Test: Amount Spent')
fig.update_traces(hoverinfo='label+percent', textinfo='value',
                  textfont_size=30,
                  marker=dict(colors=colors,
                              line=dict(color='black', width=3)))
fig.show()

# label = ["Purchases Made by Control Campaign",
#          "Purchases Made by Test Campaign"]
# counts = [sum(control_data["Purchases"]),
#           sum(test_data["Purchases"])]
# colors = ['gold', 'lightgreen']
# fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
# fig.update_layout(title_text='Control Vs Test: Purchases')
# fig.update_traces(hoverinfo='label+percent', textinfo='value',
#                   textfont_size=30,
#                   marker=dict(colors=colors,
#                               line=dict(color='black', width=3)))
# fig.show()


# figure = px.scatter(data_frame = ab_data,
#                     x="Content Viewed",
#                     y="Website Clicks",
#                     size="Website Clicks",
#                     color="Campaign Name",
#                     trendline="ols")
# figure.show()

# figure = px.scatter(data_frame = ab_data,
#                     x="Added to Cart",
#                     y="Content Viewed",
#                     size="Added to Cart",
#                     color="Campaign Name",
#                     trendline="ols")
# figure.show()

# figure = px.scatter(data_frame = ab_data,
#                     x="Purchases",
#                     y="Added to Cart",
#                     size="Purchases",
#                     color="Campaign Name",
#                     trendline="ols")
# figure.show()