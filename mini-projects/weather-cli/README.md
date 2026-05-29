# Weather-CLI

A command weather app that returns the geodata such as temperature, windspeed and time using API call from open-metro website

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