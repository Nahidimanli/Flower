from django.contrib import admin
from .models import (MyUser)

admin.site.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','bio', 'image')
    search_fields = ('username','email')
    list_filter = ('username', 'email')
   
