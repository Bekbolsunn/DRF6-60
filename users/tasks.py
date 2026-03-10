from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def add(x, y):
    sleep(30)
    print(x + y)
    return "OK"

@shared_task
def send_otp_email(email, code):
    print(10 * "#")
    send_mail(
        "Привет ДП",
        f"вот твой одноразовый код {code}",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    return "SENT"

@shared_task
def todo_homework():
    print(10 * "$")
    send_mail(
        "Привет друг",
        "Пора делать домашку",
        settings.EMAIL_HOST_USER,
        ["тутemail"],
        fail_silently=False,
    )
    return "BOLDU"
