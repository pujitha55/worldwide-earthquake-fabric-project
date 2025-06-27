#!/usr/bin/env python
# coding: utf-8

# ## 01 Worldwide Earthquake Events API - Bronze Layer Processing
# 
# New notebook

# # <mark></mark>Worldwide Earthquake Events API - Bronze Layer Processing

# In[2]:


import requests
import json

# Construct the API URL with start and end dates provided by Data Factory, formatted for geojson output.
url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={start_date}&endtime={end_date}"

# Make the GET request to fetch data
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the JSON response
    data = response.json()
    data = data['features']
    
    # Specify the file name (and path if needed)
    file_path = f'/lakehouse/default/Files/{start_date}_earthquake_data.json'
    
    # Open the file in write mode ('w') and save the JSON data
    with open(file_path, 'w') as file:
        # The `json.dump` method serializes `data` as a JSON formatted stream to `file`
        # `indent=4` makes the file human-readable by adding whitespace
        json.dump(data, file, indent=4)
        
    print(f"Data successfully saved to {file_path}")
else:
    print("Failed to fetch data. Status code:", response.status_code)

