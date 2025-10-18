# Django Blog - User Authentication System

This document outlines the implementation of the user authentication system for this blog project. The system handles user registration, login, logout, and profile management.

## Features

### 1. User Registration

* **What it does:** Allows new users to create an account.
* **How it works:**
    * Uses a custom `UserRegisterForm` in `blog/forms.py` which extends Django's `UserCreationForm` to include an email field.
    * The `register` view in `blog/views.py` handles form validation. Upon successful registration, a success message is displayed, and the user is redirected to the login page.
* **How to use:** Navigate to the `/register/` URL, fill in a unique username, a valid email, and a password, then submit the form.

### 2. User Login

* **What it does:** Allows existing users to sign into their accounts.
* **How it works:**
    * Utilizes Django's built-in `LoginView` for security and reliability.
    * The view is configured in `blog/urls.py` to use the `blog/login.html` template.
    * Upon successful login, users are redirected to the homepage, as defined by `LOGIN_REDIRECT_URL` in `settings.py`.
* **How to use:** Navigate to the `/login/` URL, enter your username and password, and submit the form.

### 3. User Logout

* **What it does:** Allows authenticated users to sign out of their accounts.
* **How it works:**
    * Uses Django's built-in `LogoutView`.
    * Upon logout, users are redirected to the homepage, as defined by `LOGOUT_REDIRECT_URL` in `settings.py`.
* **How to use:** Authenticated users can click the "Logout" link in the navigation bar.

### 4. Profile Management

* **What it does:** Allows logged-in users to view and update their profile information (username and email).
* **How it works:**
    * The `profile` view in `blog/views.py` is protected by the `@login_required` decorator, ensuring only authenticated users can access it.
    * It uses the `UserUpdateForm` from `blog/forms.py` to handle data updates.
* **How to use:** Logged-in users can navigate to the `/profile/` URL via the "Profile" link in the navigation bar to view and edit their details.

## Security

* **CSRF Protection:** All forms use the `{% csrf_token %}` template tag to protect against Cross-Site Request Forgery attacks.
* **Password Hashing:** Django's authentication system automatically handles secure password hashing and storage, so plaintext passwords are never stored in the database.

## Blog Post Management

The blog includes full CRUD (Create, Read, Update, Delete) functionality for posts.

* **Create:** Authenticated users can create new posts by clicking the "New Post" link in the navigation or by visiting the `/posts/new/` URL.
* **Read:** All users can view a list of posts on the homepage (`/`) and can view the full content of a single post by clicking its title (`/posts/<id>/`).
* **Update:** Only the original author of a post can edit it. The "Edit" link will appear on the post's detail page for the author, or they can navigate to `/posts/<id>/edit/`.
* **Delete:** Only the original author of a post can delete it. The "Delete" link will appear on the post's detail page for the author, or they can navigate to `/posts/<id>/delete/`.

Permissions are enforced using Django's `LoginRequiredMixin` for creating posts and `UserPassesTestMixin` to ensure only authors can edit or delete their own content.

## Comment System

The blog features a full comment system, allowing users to engage with posts.

* **Create:** Authenticated users can add comments to any post via the form on the post's detail page.
* **Read:** All users can view comments on a post's detail page.
* **Update:** Users can only edit their own comments. The "Edit" link will appear next to their comments.
* **Delete:** Users can only delete their own comments. The "Delete" link will appear next to their comments.

Permissions are enforced to ensure users can only modify their own content.