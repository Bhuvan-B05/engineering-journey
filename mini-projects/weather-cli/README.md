# Weather-CLI

A command-line weather application that retrieves weather information such as temperature, wind speed, and time using data from the Open-Meteo API.

# Features

- API Integration
- Nested Dictionary Navigation
- Python library used (requests)

# Technologies - meaning

* API (Application Programming Interface) - A set of rules that allows one software application to      communicate with another. In this project, the weather API receives a request from the program and returns weather data.

* JSON (JavaScript Object Notation) - A lightweight data-interchange format used to store and exchange structured data. In Python, JSON data is usually converted into dictionaries and lists.

* requests.get() - Sends an HTTP GET request to a specified URL and retrieves the response returned by the server.

* HTTP Status Code 200 - Indicates that the request was successfully processed by the server and the requested data was returned.

* Nested Dictionaries - Some values inside a dictionary can themselves be dictionaries. This allows hierarchical storage of data. In this project, weather information was extracted from the nested 'current_weather' dictionary.

# Example Output

```text
Temperature: 33.6 Celsius
Wind Speed: 9.5 km/h
Time: 2026-05-29T13:00
```