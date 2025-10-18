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
    

class FollowUserView(APIView):
    """
    Allows a user to follow another user.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        if request.user == user_to_follow:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)
        return Response({"detail": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)


class UnfollowUserView(APIView):
    """
    Allows a user to unfollow another user.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)