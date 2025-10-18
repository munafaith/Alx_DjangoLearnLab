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

## API Testing and Validation Examples

This section provides examples of how to interact with and test the API using `curl`.

### 1. Authentication

First, obtain an authentication token by logging in.

**Request:**
```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "your_username", "password": "your_password"}' [http://127.0.0.1:8000/api/login/](http://127.0.0.1:8000/api/login/)

**Success Response:**

{
    "token": "YOUR_UNIQUE_TOKEN_STRING"
}

Save this token for the next steps.

2. Creating a Post (Authenticated)
Use your token in the Authorization header to create a new post.

Request:

curl -X POST -H "Authorization: Token YOUR_UNIQUE_TOKEN_STRING" -H "Content-Type: application/json" -d '{"title": "My First Post", "content": "This is the content of my first post."}' [http://127.0.0.1:8000/api/posts/](http://127.0.0.1:8000/api/posts/)

** Success Response (Status 201 Created):**
{
    "id": 1,
    "author": "your_username",
    "title": "My First Post",
    "content": "This is the content of my first post.",
    "created_at": "2025-10-18T13:45:00.000000Z",
    "updated_at": "2025-10-18T13:45:00.000000Z"
}

"""3. Listing and Searching Posts (Unauthenticated)
Anyone can view and search for posts.

Request (List): """

curl [http://127.0.0.1:8000/api/posts/](http://127.0.0.1:8000/api/posts/)

**Success Response (Paginated):**

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "author": "your_username",
            "title": "My First Post",
            "content": "This is the content of my first post.",
            "created_at": "...",
            "updated_at": "..."
        }
    ]
}

Request (Search):

curl "[http://127.0.0.1:8000/api/posts/?search=First](http://127.0.0.1:8000/api/posts/?search=First)"

The response will be a filtered list of posts containing the word "First".

4. Testing Permissions (Updating a Post)
Only the author of a post can update it.

Request (Successful Update by Author):

curl -X PUT -H "Authorization: Token YOUR_UNIQUE_TOKEN_STRING" -H "Content-Type: application/json" -d '{"title": "My Updated Post", "content": "Updated content."}' [http://127.0.0.1:8000/api/posts/1/](http://127.0.0.1:8000/api/posts/1/)

Success Response: The updated post object is returned.

Request (Failed Update by Another User): If a different authenticated user (with a different token) tried to update post #1, they would receive the following error.

Failure Response (Status 403 Forbidden):

{
    "detail": "You do not have permission to perform this action."
}

This confirms that the IsOwnerOrReadOnly permission is working correctly.

## User Follows and Feed

The API supports following other users and viewing a chronological feed of their posts. All endpoints in this section require authentication.

### Follow a User
* **Endpoint:** `POST /api/follow/<user_id>/`
* **Description:** Adds the user specified by `user_id` to the authenticated user's "following" list.
* **Example Request:**
  ```bash
  curl -X POST -H "Authorization: Token YOUR_TOKEN" [http://127.0.0.1:8000/api/follow/2/](http://127.0.0.1:8000/api/follow/2/)
  ```
* **Success Response:** `{"detail": "You are now following <username>."}`

### Unfollow a User
* **Endpoint:** `POST /api/unfollow/<user_id>/`
* **Description:** Removes the user specified by `user_id` from the authenticated user's "following" list.
* **Example Request:**
  ```bash
  curl -X POST -H "Authorization: Token YOUR_TOKEN" [http://127.0.0.1:8000/api/unfollow/2/](http://127.0.0.1:8000/api/unfollow/2/)
  ```
* **Success Response:** `{"detail": "You have unfollowed <username>."}`

### View Your Feed
* **Endpoint:** `GET /api/feed/`
* **Description:** Returns a paginated list of the most recent posts from all users that you follow.
* **Example Request:**
  ```bash
  curl -X GET -H "Authorization: Token YOUR_TOKEN" [http://127.0.0.1:8000/api/feed/](http://127.0.0.1:8000/api/feed/)
  ```
* **Success Response:** A paginated list of post objects.

## Likes and Notifications

The API supports liking posts and receiving notifications for key events. All endpoints require authentication.

### Likes
* **Like a Post:** `POST /api/posts/<post_id>/like/`
  * Creates a like relationship and notifies the post's author.
* **Unlike a Post:** `POST /api/posts/<post_id>/unlike/`
  * Removes the like relationship.

### Notifications
* **View Notifications:** `GET /api/notifications/`
  * Returns a list of all notifications for the authenticated user.
* **Notification Triggers:** Notifications are automatically created for:
  * New followers.
  * Likes on your posts.
  * Comments on your posts.