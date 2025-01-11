from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Dummy data: username and password
users = {
    "ndus-cody": "adaeaea0-6b5c-4d7a-948d-4fa86373a522"
}


# Basic authentication function
@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username  # Authentication successful
    return None  # Authentication failed


# Protected route that requires Basic Authentication
@app.route('/api/data', methods=['GET'])
@auth.login_required
def get_data():
    # If authentication is successful, respond with data
    return jsonify({"message": "Request successful", "data": "Some data"})


if __name__ == '__main__':
    app.run(debug=True)
