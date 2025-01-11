import requests

# Example for obtaining a token (this depends on the API)
auth_url = 'http://127.0.0.1:5000/api/data'

# Send a POST request to get the token, these creds are fake, don't be stupid
auth_response = requests.get(auth_url, auth=("ndus-cody", "adaeaea0-6b5c-4d7a-948d-4fa86373a522"))


if auth_response.status_code == 200:
    result = auth_response.json()
    print(result)
else:
    print(f"Hmmm... something went wrong. Status Code: {auth_response.status_code}")
