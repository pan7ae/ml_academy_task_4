import requests


# URL of your API
API_URL = 'http://127.0.0.1:8000/recommendations/'

# Data to send in JSON format
data = {
    "user_beers": ["Budweiser", "Heineken"]  # Example list of user's beers
}

# Sending a POST request
response = requests.post(API_URL, json=data)

# Printing the response
print(response.status_code)  # Output the status code of the response
print(response.json())  # Output the response data in JSON format
