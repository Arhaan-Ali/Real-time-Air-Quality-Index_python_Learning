import json
import requests
import urllib.error
from urllib.request import urlopen

def ip_fetcher() :
    try :
      base_url = "http://ipinfo.io/json"
      response = urlopen(base_url)
      data = json.load(response)
      return {
        "ip" : data.get('ip', 'none')
    }
    except urllib.error.HTTPError as e :
      print(f"HTTP error {e.code} : {e.reason}")
    except urllib.error.URLError as e :
      print(f"Url error : {e.reason}")
    except json.JSONDecodeError as e :
      print(f"JSON Decoder Error : {e}")
    except Exception as e :
      print(f"Unexpected Error Occurred : {e}")

def location_fetcher():
    ip_data = ip_fetcher()
    try :
        base_url = "https://get.geojs.io/v1/ip/geo/" + ip_data["ip"] + ".json"
        response = requests.get(base_url)
        geo_data = response.json()
        return  {
            "country" : geo_data.get('country', 'None'),
            "state" : geo_data.get('region', 'None'),
            "city" : geo_data.get('city', 'None')
     }
    except requests.RequestException as e :
        return {"Error" : f"Error : {e}"}
    except KeyError as e :
        return {"error": f"Data Structure Error: {e}. Please check API response format."}


if __name__ == "__main__" :
   ip_fetcher()
   location_fetcher()
