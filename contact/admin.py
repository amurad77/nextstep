from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactdAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'email', 'message', 'created_at', )
    list_filter = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'created_at', 'updated_at')
admin.site.register (Contact, ContactdAdmin)