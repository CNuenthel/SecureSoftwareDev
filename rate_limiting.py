"""
This is a basic app with server side rate limiting
"""

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

app = Flask(__name__)
SECRET_KEY = os.getenv('SECRET_KEY')

# Build Limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"
)


# Overwrites default limits and only allows 1 endpoint request a day
@app.route("/slow")
@limiter.limit("1 per day")
def slow():
    return ":("


# Does not overwrite default limits while applying a 1 per second request limit
@app.route("/medium")
@limiter.limit("1/second", override_defaults=False)
def medium():
    return ":|"


# No limits
@app.route("/fast")
def fast():
    return ":)"


@app.route("/ping")
@limiter.exempt
def ping():
    return "PONG"


if __name__ == '__main__':
    app.run(debug=True)
