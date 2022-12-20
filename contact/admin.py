from django.contrib import admin
from .models import Contact, Apply
# Register your models here.


class ContactdAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'email', 'message', 'created_at', )
    list_filter = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'created_at', 'updated_at')
admin.site.register (Contact, ContactdAdmin)

class ApplydAdmin(admin.ModelAdmin):
    list_display = ('name_surname', 'number', 'email', 'project_name', 'project_des', 'team_members', 'project_level', 'created_at', )
    list_filter = ('name_surname', 'created_at', 'updated_at')
    search_fields = ('name_surname', 'created_at', 'updated_at')
admin.site.register (Apply, ApplydAdmin)