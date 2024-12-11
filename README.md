
# AQI_mate 

AQI-mate is a project designed to provide real-time air quality information based on a user's current location. The project consists of two main files:

location_fetcher.py - Responsible for obtaining the user's location using APIs.
aqi_fetcher.py - Fetches air quality data based on the retrieved location details.



##  File Discription :
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
## API Reference

IPfy API: https://www.ipify.org/

GeoJS API: https://www.geojs.io/

IQAir API: https://www.iqair.com/


## Future Integrations 

Add a graphical interface.

Enhance error handling for API failures.

Implement caching to reduce API requests.


## License

MIT License

Copyright (c) [2024] [Arhaan Ali]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

