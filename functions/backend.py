import requests as rq
API_KEY = "6e247dcf3b8fd4e3713400b02f504095"

def get_remote_data(place, forecast_days, weather_attribute):
    # See Find API Key below
    # See Find API below
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={
    API_KEY}"
    response = rq.get(url)
    data = response.json()

    filtered_data = data["list"]

    return filtered_data

if __name__ == "__main__":
    data = get_remote_data("Tokyo", 1, "Temperature")
    print(data)

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