import streamlit as slt
import plotly.express as pltexp
slt.title("Weather forecast for the Next (Max 10) Days")
place = slt.text_input("Place:")
forecast_days = slt.slider("Forecast Days", min_value=1, max_value=5,
                           step=1, help="Select number of days to "
                                                 "forecast")
data_option = slt.selectbox("Select data to view", ("Temperature", "Sky"))

slt.subheader(f"{data_option} for the next {forecast_days} days in {place}")

dates = ["2025-10-09", "2025-10-10", "2025-10-11"]
temperatures = [10, 11, 15]
graph = pltexp.line(x=dates, y=temperatures, labels={"x":"Date",
                                                     "y":"Temperature (C)"})
slt.plotly_chart(graph)

