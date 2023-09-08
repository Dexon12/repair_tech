from django.contrib import admin

from .models import *

class ServicesAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}


admin.site.register(Services, ServicesAdmin)