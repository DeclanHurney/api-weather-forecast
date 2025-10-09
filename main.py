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

if place:
    # Get the temperature/sky data
    # dates, temperatures = bkd.get_local_data(forecast_days)
    try:
        filtered_data = bkd.get_remote_data(place, forecast_days)

        if data_option == "Temperature":
            # Create a temperature plot
            temperatures = [dict['main']['temp'] / 10 for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            # print(f"temperatures 1: {temperatures}")
            # # temperature = [images[temperature] for temperature in temperatures]
            # temperatures = [temperature / 10 for temperature in temperatures]
            # print(f"temperatures 2: {temperatures}")
            graph = plty_exp.line(x=dates, y=temperatures, labels={"x": "Date",
                                                                 "y":"Temperature (C)"})
            slt.plotly_chart(graph)
        if data_option == "Sky":
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            images = {"Clear": "images/clear.png", "Clouds":
                "images/cloud.png","Rain": "images/rain.png", "Snow":
                "images/snow.png"}
            sky_images = [images[condition] for condition in sky_conditions]
            # print(f"sky_conditions: {sky_conditions}")
            # print(f"sky_images: {sky_images}")
            # ['Clouds', 'Clouds', 'Clear', 'Clear', 'Clouds', 'Clouds', 'Clouds',
            #  'Clouds']
            slt.image(sky_images, width=115)
    except KeyError:
        slt.warning(f"No data for this place {place}. Check spelling and try again.")

