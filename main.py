import streamlit as slt
import plotly.express as plty_exp
from functions import backend as bkd

slt.title("Weather forecast for the Next (Max 10) Days")

# Here are the four pieces of input sent by the user
# 1: place (string) 2: forecast_days (integer) 3: Temperature or Sky (string)
place = slt.text_input("Place:")
forecast_days = slt.slider("Forecast Days", min_value=1, max_value=5,
                           step=1, help="Select number of days to "
                                                 "forecast")
data_option = slt.selectbox("Select data to view", ("Temperature", "Sky"))



slt.subheader(f"{data_option} for the next {forecast_days} days in {place}")

dates, temperatures = bkd.get_local_data(forecast_days)

graph = plty_exp.line(x=dates, y=temperatures, labels={"x": "Date",
                                                     "y":"Temperature (C)"})
slt.plotly_chart(graph)

