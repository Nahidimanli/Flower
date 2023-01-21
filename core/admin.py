from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import (
    Contact, Setting,  ContactUs, Gallery, About, Why, Customer, Blog
)


#admin.site.register(Contact)
admin.site.register(Setting)
admin.site.register( ContactUs)
admin.site.register(Gallery)
admin.site.register(About)
admin.site.register(Why)
admin.site.register(Customer)
admin.site.register(Blog)




@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_check')
    list_filter = ('is_check',)
    readonly_fields = ('email',)