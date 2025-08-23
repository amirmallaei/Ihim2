import uuid
from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.core.cache import cache
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string




User = get_user_model()

@shared_task
def send_activation_link(user_id):
    user = User.objects.filter(id=user_id).first()
    otp = "Activation_"+str(uuid.uuid4())
    link = 'http://192.168.100.32:8000/user/activate/'+otp
    email_text = render_to_string('emails/activation_link.html', {'name':user.get_full_name,
                                                            'link':link})
    cache.set( otp, user.id, 300)#{otp:user.id}
    print(f"{otp=} {user.id=}")
    email = EmailMultiAlternatives(f"Welcome {user.first_name},","",  "amirmallaei@gmail.com", [str( user.email)])
    email.attach_alternative(email_text, 'text/html')
    email.send()


@shared_task
def greet_user_email(user_id):
    user = User.objects.filter(id=user_id).first()
    email_text = render_to_string('emails/greetings.html', {'name':user.get_full_name})
    email = EmailMultiAlternatives(f"Hooray {user.first_name},","",  "amirmallaei@gmail.com", [str( user.email)])
    email.attach_alternative(email_text, 'text/html')
    email.send()


