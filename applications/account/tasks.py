from decouple import config
from django.core.mail import send_mail
from config.celery import app


@app.task
def send_user_activation_link(email, activation_code):
    full_link = f'http://localhost:8000/api/v1/account/activate/{activation_code}'
    send_mail(
        'from electronic store',
        f'Your activation link {full_link}',
        config('EMAIL_HOST_USER'),
        [email]
    )


@app.task
def send_forgot_password_code(email, activation_code):
    send_mail(
        'from electronic store',
        f'Your code to change password {activation_code}',
        config('EMAIL_HOST_USER'),
        [email]
    )
