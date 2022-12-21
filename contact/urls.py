from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'fileapp'


urlpatterns = [
    path("apply/", views.apply),
    path("upload", views.send_files, name='uploads')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)