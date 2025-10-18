from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from .models import CustomUser

class RegisterView(generics.CreateAPIView):
    """
    Handles user registration. The serializer now handles token creation.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class ProfileView(APIView):
    """
    A simple view for authenticated users to see their profile.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)