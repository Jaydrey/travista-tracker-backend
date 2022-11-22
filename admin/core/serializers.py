from rest_framework import  serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "pk",
            "email",
            "phone_number",
            "user_type",
            "ratings",
            "username",
            "first_name",
            "last_name",
        )

class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    phone_number = serializers.CharField(max_length=15)
    user_type = serializers.CharField(max_length=10)
    password  =serializers.CharField(max_length=100)
    business_name = serializers.CharField(max_length=100)

class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)
