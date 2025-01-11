from flask import Flask, jsonify, request
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

# Simulating a database of users with their API tokens
users = {
    "user1": "secret_token_1",
    "user2": "secret_token_2"
}


# Token verification function
@auth.verify_token
def verify_token(token):
    for username, api_token in users.items():
        if token == api_token:
            return username
    return None


@app.route('/data', methods=['GET'])
@auth.login_required
def get_data():
    """ Endpoint that requires token authentication """
    return jsonify({"message": f"Hello, {auth.current_user()}! Here's some protected data."})


if __name__ == '__main__':
    app.run(debug=True)
