from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token 

# Get the custom user model using Django's recommended function
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration that also handles token creation.
    """
    email = serializers.EmailField(required=False)
    token = serializers.CharField(read_only=True) # Field to return the token

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio', 'profile_picture', 'token']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            bio=validated_data.get('bio', '')
        )
        token = Token.objects.create(user=user)
        # Add the token to the instance so it can be returned in the response
        user.token = token.key
        return user