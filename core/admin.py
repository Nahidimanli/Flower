
# Register your models here.
from django.contrib import admin


from .models import (
    Contact, Setting, Gallery, About, Why, Customer, Blog, Advertisement, ContactUs,Catagory,Shop

)

from  embed_video.admin  import  AdminVideoMixin
from .models  import  tutorial
#Register your models here.

class  tutorialAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(tutorial, tutorialAdmin)

#admin.site.register(Contact)
admin.site.register(Setting)
admin.site.register(ContactUs)
admin.site.register(Gallery)
admin.site.register(About)
admin.site.register(Why)
admin.site.register(Customer)
#admin.site.register(Blog)
admin.site.register(Advertisement)
admin.site.register(Catagory)
admin.site.register(Shop)





@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_check')
    list_filter = ('is_check',)
    readonly_fields = ('email',)


@admin.register(Blog)
class BlogtAdmin(admin.ModelAdmin):
    list_display = ('title', 'title', 'description')
    search_fields = ('title',)
    


admin.site.site_header = 'Flower shop'