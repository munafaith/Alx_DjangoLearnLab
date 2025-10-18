# accounts/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration that also handles token creation.
    """
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    token = serializers.CharField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'bio', 'profile_picture', 'token']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            bio=validated_data.get('bio', '')
        )
        token = Token.objects.create(user=user)
        user.token = token.key
        return user
    
    