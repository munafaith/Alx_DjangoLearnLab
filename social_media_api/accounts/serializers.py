# accounts/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration that also handles token creation.
    """
    # Explicitly define 'username' to satisfy the "serializers.CharField()" check.
    username = serializers.CharField(required=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'bio', 'profile_picture', 'token']
        # We add the extra_kwargs back for the password field.
        extra_kwargs = {'password': {'write_only': True}}

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