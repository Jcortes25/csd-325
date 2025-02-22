import requests

# Replace with your actual API key
api_key = 'your_api_key_here'
city = 'London'

# URL to get weather data
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

# Test connection
response = requests.get(url)
print("Connection Status:", response.status_code)

# Print the raw JSON response
print("Raw Response:", response.json())

# Parse the response and format the output
data = response.json()
main_weather = data['weather'][0]['description']
temperature = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius

print("\nFormatted Weather Data:")
print(f"City: {city}")
print(f"Weather: {main_weather}")
print(f"Temperature: {temperature:.2f}°C")
