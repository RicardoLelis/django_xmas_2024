import uuid
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

def generate_unique_username(email):
    """
    Generate a unique username based on the email address.
    """
    unique_suffix = uuid.uuid4().hex[:8]  # Generate a random 8-character suffix
    return f"{email.split('@')[0]}_{unique_suffix}"

def generate_email_verification_token(user):
    """
    Generate a JWT token for email verification.
    The token will include the user ID and will expire in 24 hours.
    """
    payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(hours=24),  # Token expires in 24 hours
        'iat': datetime.utcnow(),  # Issued at current time
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

def decode_email_verification_token(token):
    """
    Decode and verify the email verification token.
    Returns the user ID if the token is valid, else None.
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user_id = payload.get('user_id')
        return user_id if user_id else None
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError) as e:
        print(f"Error during token decoding: {e}")
        return None
