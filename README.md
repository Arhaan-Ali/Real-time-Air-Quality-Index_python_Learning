#AQI_mate - Project README
Overview
AQI Fetcher is a project designed to provide real-time air quality information based on a user's current location. The project consists of two main files:

location_fetcher.py - Responsible for obtaining the user's location using APIs.
aqi_fetcher.py - Fetches air quality data based on the retrieved location details.
File Descriptions
1. location_fetcher.py
This file utilizes two APIs to determine the user's location:

IPfy API:
This API retrieves the user's public IP address.

GeoJS API:
Using the IP address obtained from IPfy, this API returns detailed location data, including country, city, and state.

Workflow:

Fetch the IP address using IPfy.
Send the IP address to GeoJS.
Extract the user's country, city, and state from the GeoJS response.
Share this data with aqi_fetcher.py.
2. aqi_fetcher.py
This file fetches air quality data using the IQAir API.

Data Retrieved:

Air Quality Index (AQI)
Location details (country, city, state)
Temperature
Humidity
Time of data retrieval
Workflow:

Receive location details from location_fetcher.py.
Use the IQAir API to fetch air quality data.
Display relevant environmental data such as AQI, temperature, and humidity.
How to Run
Ensure Python and required libraries are installed.
Run location_fetcher.py to get the user's location.
Automatically pass the location to aqi_fetcher.py to display the air quality details.
API References
IPfy API: https://www.ipify.org/
GeoJS API: https://www.geojs.io/
IQAir API: https://www.iqair.com/
Future Enhancements
Add a graphical interface.
Enhance error handling for API failures.
Implement caching to reduce API requests.
License
This project is open-source and available under the MIT License.

By following this structure, the README file ensures clarity, explaining the project's functionality, structure, and external API usage.







