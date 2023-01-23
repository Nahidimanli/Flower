from django.template import Library
from core.models import Contact, Advertisement


register = Library

@register.simple_tag
def get_contact_all():
    return Contact.objects.all()


@register.simple_tag
def get_advertisement_all():
    return Advertisement.objects.all()

