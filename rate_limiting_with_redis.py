from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from redis import Redis

"""
To start redis in your linux-based OS:

# Install Redis Server
sudo apt update
sudo apt install redis-server

# Verify Redis is running
redis-cli

# If redis was not shown as running on port 6379;
# Start the service, 
sudo service redis-server start

# Then verify that redis is running

"""
app = Flask(__name__)

# Initialize Redis client
redis_client = Redis(host='localhost', port=6379, db=0)

# Initialize Flask-Limiter with Redis storage
limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri="redis://localhost:6379/0"
)


@app.route("/limited")
@limiter.limit("5 per minute")
def limited_route():
    return "This route is rate limited to 5 requests per minute."


if __name__ == "__main__":
    app.run(debug=True)
