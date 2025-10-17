
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    Represents a single blog post.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    # on_delete=models.CASCADE means if a User is deleted, their posts are deleted too.
    # related_name='posts' lets us find all posts by a user, e.g., user.posts.all()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title