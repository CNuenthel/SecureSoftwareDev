import requests

# The URL of the Flask app
url = "http://127.0.0.1:5000/data"

# Set the token for authentication (use a valid token from the app)
headers = {
    "Authorization": "Bearer secret_token_1"  # Change this to "secret_token_2" for user2
}

# Make a GET request with the Authorization header
response = requests.get(url, headers=headers)

# Check the status and print the response
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Error:", response.status_code, response.text)
