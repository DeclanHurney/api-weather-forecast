from unittest import case
import streamlit as slt
import requests as rq
from dateutil.rrule import weekday

API_KEY = "6e247dcf3b8fd4e3713400b02f504095"

def get_remote_data(place, forecast_days):
    # See Find API Key below
    # See Find API below
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={
    API_KEY}"
    # print(url)
    response = rq.get(url)
    data = response.json()
    # A reading is taken every three hours, 8 readings will be (taken in a day,
    # that is 40 readings over 5 weeks. Following list will contain 40 entries
    message = data["message"]
    if message != "city not found":
        print(f"Response from API - {message}. Please check {place}")

    filtered_data = data["list"]
    # But we only want the no of readings for the no of days entered by
    # user. Therefore, 8 x number of days will tell us this
    number_of_readings = 8 * forecast_days
    # We can slice down the size of the filtered_data to the number we want
    filtered_data = filtered_data[:number_of_readings]
    # if weather_attribute is not None and len(weather_attribute) > 0:
    #     # We can further filter the filtered_data to the kind of weather we want
    #     match weather_attribute:
    #         case "Temperature":
    #             return filtered_data[0]["temp"]
    #         case "Sky":
    #             return filtered_data[0]["weather"]
    return filtered_data

if __name__ == "__main__":
    data = get_remote_data("Tokyok", 2)
    # data = data["temp"] / 10
    print(f"data: {data}")

def get_local_data(days):
    dates_list = ["2025-10-09", "2025-10-10", "2025-10-11"]
    temperatures_list = [10, 11, 15]
    temperatures_list = [days * i for i in temperatures_list]
    return dates_list, temperatures_list

# Find API
# 1) https://home.openweathermap.org/
# 2) Under username, My API Keys

# Find API
# 1) https://home.openweathermap.org/
# 2) API
# 3) Under 5 Day / 3 Hour Forecast Choose API doc
# 4) Click on Built-in API request by city name
# 5) Assign the API Call value into the url variable