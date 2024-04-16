from django.contrib import admin
from core.models import ContactUs

# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']

admin.site.register(ContactUs, ContactUsAdmin)

