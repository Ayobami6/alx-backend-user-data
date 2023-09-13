#!/usr/bin/env python3
""" Simple flask app
"""

from flask import (Flask, jsonify, request, abort, redirect)
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
    try:
        user = AUTH.register_user(email, passwd)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": f"{email}", "message": "user created"})


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> dict:
    """ Login user and create a session
    """
    data = request.form
    email = data['email']
    passwd = data['password']
    if AUTH.valid_login(email, passwd):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": f"{email}", "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> dict:
    """ Logout user session
    """
    session_id = request.cookies.get("session_id", None)
    # get user from session id
    user = AUTH.get_user_from_session_id(session_id)
    if not user or session_id is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
