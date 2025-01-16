# signals.py
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

User = get_user_model()

@receiver(post_save, sender=User)
def send_registration_email(sender, instance, created, **kwargs):
    if created:
        subject = "Welcome to Egerton CU!"
        message = f"Hi {instance.username},\n\nThank you for registering . We're excited to have you onboard!"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]

        send_mail(subject, message, from_email, recipient_list)
