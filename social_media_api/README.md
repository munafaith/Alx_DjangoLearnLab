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

## Posts and Comments API

The API supports full CRUD operations for posts and comments.

### Posts
* **List/Create Posts:** `GET` or `POST` to `/api/posts/`
* **Retrieve/Update/Delete a Post:** `GET`, `PUT/PATCH`, or `DELETE` to `/api/posts/<id>/`
* **Search Posts:** `GET` to `/api/posts/?search=your_keyword`
* **Permissions:** All users can view posts. Only authenticated users can create posts. Only the author of a post can edit or delete it.

### Comments
* **List/Create Comments:** `GET` or `POST` to `/api/comments/`
* **Retrieve/Update/Delete a Comment:** `GET`, `PUT/PATCH`, or `DELETE` to `/api/comments/<id>/`
* **Permissions:** All users can view comments. Only authenticated users can create comments. Only the author of a comment can edit or delete it.

**Note:** Creating, updating, or deleting content requires an `Authorization: Token <your_token>` header in your request.