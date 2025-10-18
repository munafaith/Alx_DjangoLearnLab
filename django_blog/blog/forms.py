
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post 

class UserRegisterForm(UserCreationForm):
    """
    A form for user registration that includes an email field.
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class UserUpdateForm(forms.ModelForm):
    """
    A form for users to update their profile information (username and email).
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
        
class PostForm(forms.ModelForm):
    """
    A form for creating and updating Post objects.
    """
    class Meta:
        model = Post
        fields = ['title', 'content']