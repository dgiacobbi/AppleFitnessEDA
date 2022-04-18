import pandas as pd
import requests
import json

def load_weather_api():

     # Using MeteoStatAPI, get the weather data for the past year in Spokane with station id
    weather_url = "https://meteostat.p.rapidapi.com/stations/daily"

    weather_key = "48c6248dd3msh5bf7b8a377bd25cp19e73ajsn114ccda534b5"
    weather_headers = {"x-rapidapi-key": weather_key}
    weather_query = {"station": INSERT_STATION_ID, "start": "2021-12-26", "end": "2022-04-12"}

    weather_response = requests.get(url=weather_url, headers=weather_headers, params=weather_query)

    # Parse through json object and storel data in dataframe for return
    weather_json_obj = json.loads(weather_response.text)
    weather_data_list = weather_json_obj["data"]

    daily_weather_df = pd.DataFrame(weather_data_list)

    return daily_weather_df