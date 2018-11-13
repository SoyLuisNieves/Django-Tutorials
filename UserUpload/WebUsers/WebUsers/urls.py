from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
 
    url(r'^uploadfiles/', include('uploadfiles.urls')),
 
]
 
# if the DEBUG is on in settings, then append the urlpatterns as below
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)