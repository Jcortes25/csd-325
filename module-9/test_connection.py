import requests

# URL to test the connection
response = requests.get('http://www.google.com')

# Output the HTTP status code (200 indicates success)
print(response.status_code)
