## User Authentication Service in Python

This project provides a simple user authentication service written in Python. The service uses Flask to create a RESTful API that allows users to register, login, and logout. The service also includes a database to store user information.

### Getting Started

To get started with the user authentication service, you will need to install the following dependencies:

* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [Flask-Login](https://flask-login.readthedocs.io/en/latest/)

Once you have installed the dependencies, you can create a new project directory and initialize a virtual environment. Then, you can install the project dependencies by running the following command:

```
pip install -r requirements.txt
```

Next, you can create a new database and initialize the schema by running the following commands:

```
python manage.py db init
python manage.py db migrate
```

Finally, you can start the user authentication service by running the following command:

```
python manage.py runserver
```

The service will be available on port 5000. You can test the service by visiting the following URL in your browser:

```
http://localhost:5000/api/v1/users/register
```

### Usage

The user authentication service provides the following endpoints:

* `/api/v1/users/register`: This endpoint allows users to register for a new account.
* `/api/v1/users/login`: This endpoint allows users to login to their account.
* `/api/v1/users/logout`: This endpoint allows users to logout of their account.

To use the endpoints, you will need to send a JSON payload with the following format:

```
{
  "username": "your_username",
  "password": "your_password"
}
```

For example, the following payload can be used to register a new user:

```
{
  "username": "johndoe",
  "password": "password123"
}
```

The service will return a JSON response with the following format:

```
{
  "success": true,
  "message": "User successfully registered"
}
```

If the request is invalid, the service will return a JSON response with the following format:

```
{
  "success": false,
  "message": "Invalid request"
}
```

### License

The user authentication service is licensed under the MIT License.

### Acknowledgments

The user authentication service was inspired by the following resources:

* [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [Flask-Login](https://flask-login.readthedocs.io/en/latest/)