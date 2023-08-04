from django.core.mail import send_mail
import random
from django.conf import settings
import pyotp
import base64
from .models import User
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# def send_mail(email):
#     subject = f'Account credentials'
#     user = User.objects.get(email=email)
#     message = f'Your OTP is {user.email} {user.password}'
#     email_from = settings.EMAIL_HOST_USER 
#     recipient_list = [email]
#     html_message = render_to_string('email_templates/credentials_email.html', {'user': user})
#     text_message = strip_tags(html_message)
#     send_mail(subject, text_message, email_from, recipient_list, fail_silently=False, html_message=html_message)
  
  
def send_user_credentials_email(username, email, password):
    subject = 'Your Account Credentials'
    message = f'Hello {username},\n\nYour account has been created with the following credentials:\n\nUsername: {username}\nPassword: {password}\n\nPlease keep your credentials safe and do not share them with anyone.\n\nThank you!'
    from_email = settings.EMAIL_HOST_USER   # Replace with your email address or a verified sender
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)