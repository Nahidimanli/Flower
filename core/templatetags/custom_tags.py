from django.template import Library
from core.models import Contact, Advertisement, Gallery


register = Library()

@register.simple_tag
def get_contact_all():
    return Contact.objects.all()


@register.simple_tag
def get_advertisement_all():
    return Advertisement.objects.all()

@register.simple_tag
def get_advertisement_count():
    return Advertisement.objects.count()

@register.simple_tag
def get_gallery_all():
    return Gallery.objects.all()

