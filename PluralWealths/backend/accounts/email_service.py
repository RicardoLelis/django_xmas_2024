from django.core.mail import send_mail
from django.conf import settings

def send_verification_email(user, verification_url):
    subject = "Verify Your Email Address - PluralWealths"
    message = f"""
    Hi {user.email},
    Please verify you email by clicking the link below:
    {verification_url}

    If you didn't sign up for this account, please ignore this email
    """

    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])