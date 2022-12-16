from django.contrib import admin
from .models import Events, Announcer


# Register your models here.
class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at' )
    list_filter = ('title', 'description', 'created_at' )
    search_fields = ('title', 'description', 'created_at')
admin.site.register (Events, EventsAdmin)


class AnnouncerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at' )
    list_filter = ('name', 'description', 'created_at' )
    search_fields = ('name', 'description', 'created_at')
admin.site.register (Announcer, AnnouncerAdmin)