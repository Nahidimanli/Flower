from core.models import Gallery, Setting
def header_and_footer(request):
    gallerys = Gallery.objects.all()
    icons =Setting.objects.all()
    context = {
        'point' : gallerys,
        "icons" : icons,
    }
    return context