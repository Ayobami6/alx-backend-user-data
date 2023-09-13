#!/usr/bin/env python3
""" Simple flask app
"""

from flask import Flask, jsonify, request
from auth import Auth

app: Flask = Flask(__name__)

AUTH: Auth = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def home() -> dict:
    """ / endpoint

    Returns:
        dict: json object
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_user() -> dict:
    """ Register user endpoint

    Returns:
        dict: json response
    """
    # get the json payload data
    data = request.form
    email = data['email']
    passwd = data['password']
    # hash the password
    # hashed_password = AUTH._hash_password(passwd)
    try:
        user = AUTH.register_user(email, passwd)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": f"{email}", "message": "user created"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
