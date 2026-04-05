from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_welcome_email(username, email):
    send_mail(
        subject='Welcome to the World Karate Federation!',
        message=f'Hi {username},\n\nWelcome to the World Karate Federation. Your account has been successfully created.\n\nOsu!',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
    )
