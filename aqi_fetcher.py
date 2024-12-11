import requests
from location import location_fetcher

def aqi_fetcher(apikey, country, state, city) :
    try :
      base_url = "http://api.airvisual.com/v2/city"
      params = {
        "key": apikey,
        "country": country,
        "state": state,
        "city": city
      }
      response = requests.get(base_url, params=params)
      response.raise_for_status()

      data = response.json()
      if data.get("status") == "success":
        current_data = data["data"]["current"]
        pollution_data = current_data["pollution"]
        weather_data = current_data["weather"]
        return {
            "location": f"{city.title()}, {state.title()}, {country.title()}",
            "AQI": pollution_data.get("aqius"),
            "temperature": weather_data.get("tp"),
            "humidity": weather_data.get("hu"),
            "timestamp": pollution_data.get("ts", "timestamp not available")
        }
      else:
        return {"Error": "Unable to Receive data"}

    except requests.RequestException as e:
     return {"Error": f"Error : {e}"}
    except KeyError as e:
     return {"error": f"Data Structure Error: {e}. Please check API response format."}

if __name__ == "__main__":
    location_data = location_fetcher()
    Apikey = "7da56f99-9f24-437a-a017-21b178b360d7"
    Country = location_data["country"]
    State  = location_data["state"]
    City = location_data["city"]
    result = aqi_fetcher(Apikey, Country, State, City)
    print("====== Air Quality Information ======")
    print(f"Timestamp : {result.get("timestamp", "Not available")}")
    print(f"City: {City.title()}, State: {State.title()}, Country:"
          f" {Country.title()}")
    print(f"Air Quality Index (AQI): {result["AQI"]}")
    print(f"Temperature : {result["temperature"]}°C")
    print(f"humidity: {result["humidity"]}%")
    print("=====================================")