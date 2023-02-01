from time import sleep

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect

from .models import VerificationModel
from random import randint


def send(email, code):
    try:
        send_mail(
        subject='Verify Code',
        message=str(code),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
    except:
        return redirect('home:main')
    return code


