import uuid
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import EmailVerificationToken
from .utils import generate_unique_username 

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate_email(self, value):
        # You can add any email validation logic here
        return value

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']

        # Generate the username using the email
        username = generate_unique_username(email)

        # Create the user with the generated username and the given email and password
        user = User.objects.create_user(
            email=email,
            password=password,
            username=username,  # Ensure username is passed
            is_active=False  # User is inactive initially
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = User.objects.filter(email=email).first()

        if not user:
            raise serializers.ValidationError("Invalid credentials.")
        if not user.is_active:
            raise serializers.ValidationError("User account is not active. Please verify your email.")
        if not user.check_password(password):
            raise serializers.ValidationError("Invalid credentials.")

        # Generate access and refresh tokens (assuming JWT is used)
        from rest_framework_simplejwt.tokens import RefreshToken

        refresh = RefreshToken.for_user(user)
        attrs['access'] = str(refresh.access_token)
        attrs['refresh'] = str(refresh)

        return attrs


class VerifyEmailSerializer(serializers.Serializer):
    """
    Serializer for email verification.
    """
    token = serializers.CharField()

    def validate(self, attrs):
        token = attrs.get('token')
        verification_token = EmailVerificationToken.objects.filter(token=token).first()

        if not verification_token:
            raise serializers.ValidationError("Invalid token.")
        if verification_token.is_expired:
            raise serializers.ValidationError("Token has expired.")
        
        # Activate user and delete the token
        user = verification_token.user
        user.is_active = True
        user.save()
        verification_token.delete()

        return {"message": "Email verified successfully."}
