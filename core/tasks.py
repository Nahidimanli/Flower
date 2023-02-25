
from celery import shared_task
from .models import ContactUs
from django.core.mail import EmailMultiAlternatives
from django.conf import settings



@shared_task
def send_mail_to_ContactUs():
    email_list = ContactUs.objects.all().values_list('email',flat=True)
    mail_text = f"Hello, <br> This is a test mail. <br> Thanks, <br> <h1>Admin</h1>"

    msg = EmailMultiAlternatives(subject='Test subject', body=mail_text, from_email=settings.EMAIL_HOST_USER, to=email_list, )
    msg.attach_alternative(mail_text, "text/html")
    msg.send()


send_mail_to_ContactUs.delay()