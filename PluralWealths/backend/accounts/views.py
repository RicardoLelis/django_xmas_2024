
from datetime import timedelta
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
import jwt
from django.conf import settings

from .serializers import UserRegisterSerializer, UserLoginSerializer
from .utils import generate_email_verification_token
from .models import EmailVerificationToken


User = get_user_model()

# Helper function to decode email verification token
def decode_email_verification_token(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload.get('user_id')
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


class UserRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Validate user registration data
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            # Save user data and create user instance
            user = serializer.save()

            # Generate the email verification token using the utility function
            token = generate_email_verification_token(user)

            # Create the EmailVerificationToken object
            # Ensure that `user` is a User instance
            verification_token = EmailVerificationToken.objects.create(
                user=user,  # User should be an instance of the User model
                token=token,
                expires_at=timezone.now() + timedelta(hours=24)  # Set expiration to 24 hours
            )

            # Construct the email verification URL
            verification_url = f"http://localhost:8000/api/verify-email/?token={verification_token.token}"

            # Send the verification email to the user
            send_mail(
                subject="Verify Your Email",
                message=f"Click the link below to verify your email:\n\n{verification_url}",
                from_email="no-reply@example.com",
                recipient_list=[user.email],
                fail_silently=False,
            )

            return Response(
                {"message": "Registration successful. Check your email for verification."},
                status=status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        token = request.query_params.get('token')
        if not token:
            return Response({"error": "Token is missing."}, status=status.HTTP_400_BAD_REQUEST)

        # Decode and verify the token
        user_id = decode_email_verification_token(token)
        if user_id:
            user = get_object_or_404(User, id=user_id)
            if user.is_active:
                return Response({"message": "User is already active."}, status=status.HTTP_200_OK)
            user.is_active = True
            user.save()
            return Response({"message": "Email verified successfully. You can now log in."}, status=status.HTTP_200_OK)
        
        return Response({"error": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
