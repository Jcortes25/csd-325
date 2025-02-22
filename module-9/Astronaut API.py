import requests

# API URL to fetch data about current astronauts
url = 'http://api.open-notify.org/astros.json'

# Make the GET request to the API
response = requests.get(url)

# Print raw JSON response
print("Raw Response:", response.json())

# Extract the list of astronauts from the response and format it
astronauts = response.json()['people']

# Output formatted data
print("\nFormatted Astronauts List:")
for astronaut in astronauts:
    print(f"Name: {astronaut['name']}, Craft: {astronaut['craft']}")
