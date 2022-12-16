from django.contrib import admin
from .models import Contact, Mentors, Trainers
# Register your models here.


class ContactdAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'email', 'message', 'created_at', )
    list_filter = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'created_at', 'updated_at')
admin.site.register (Contact, ContactdAdmin)


class MentorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'work', 'linkedin_link', 'created_at' )
    list_filter = ('name', 'work', 'linkedin_link', 'created_at' )
    search_fields = ('name', 'work', 'linkedin_link', 'created_at' )
admin.site.register (Mentors, MentorsAdmin)

class TrainersAdmin(admin.ModelAdmin):
    list_display = ('name', 'work', 'linkedin_link', 'created_at' )
    list_filter = ('name', 'work', 'linkedin_link', 'created_at' )
    search_fields = ('name', 'work', 'linkedin_link', 'created_at' )
admin.site.register (Trainers, TrainersAdmin)