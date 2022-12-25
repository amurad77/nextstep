from django.contrib import admin
from .models import Contact, Apply
# Register your models here.


class ContactdAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'email', 'message', 'created_at', )
    list_filter = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'created_at', 'updated_at')
admin.site.register (Contact, ContactdAdmin)

class ApplydAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'number', 'email', 'what_idea', 'hours', 'idea', 'people', 'industries1', 'industries2', 'areas1', 'areas1', 'file', 'created_at', )
    list_filter = ('name', 'surname', 'created_at', 'updated_at')
    search_fields = ('name', 'surname', 'created_at', 'updated_at')
admin.site.register (Apply, ApplydAdmin)