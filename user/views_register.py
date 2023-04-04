from django.core.mail import send_mail
import requests

def register_user (requests):
    send_mail(
    'Subject here',
    'Here is the message.',
    'jarukorn8lumchom@gmail.com',
    ['jarukorn8lumchom@gmail.com'],
    fail_silently=False,
)