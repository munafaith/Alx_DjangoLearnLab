# Social Media API

This is the backend API for a social media application built with Django and Django REST Framework.

## Setup and Installation

1.  Clone the repository.
2.  Install dependencies: `pip install django djangorestframework Pillow`
3.  Run migrations: `python manage.py migrate`
4.  Start the server: `python manage.py runserver`

## User Authentication

### User Model
The API uses a custom user model which includes fields for `bio`, `profile_picture`, and `followers`.

### Registration
* **Endpoint:** `POST /api/register/`
* **Body:** `{ "username": "your_username", "password": "your_password", "email": "optional@email.com" }`
* **Success Response:** Returns the new user object and an authentication token.

### Login
* **Endpoint:** `POST /api/login/`
* **Body:** `{ "username": "your_username", "password": "your_password" }`
* **Success Response:** Returns the user's authentication token.