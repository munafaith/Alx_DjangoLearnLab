from rest_framework import generics
from .serializers import UserSerializer
from .models import CustomUser

class RegisterView(generics.CreateAPIView):
    """
    Handles user registration. The serializer now handles token creation.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer