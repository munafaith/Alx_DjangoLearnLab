from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from .models import CustomUser

class RegisterView(generics.CreateAPIView):
    """
    Handles user registration and returns a token upon success.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)