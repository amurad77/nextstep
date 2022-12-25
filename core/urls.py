from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'fileappcore'


urlpatterns = [
    path("", views.index),
    path("events/", views.events),
    path("about/", views.about),
    path("incubation-program/", views.incubation),
    path("event-detail/<slug:slug>/", views.event_detail, name='events_details'),

    # path("upload", views.send_files, name='uploads')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)