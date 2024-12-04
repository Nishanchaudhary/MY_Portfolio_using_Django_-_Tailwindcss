from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [ 
    path('', home, name='home'),
    path('about', about, name='about'),
    path('skills', skills, name='skills'),
    path('service', service, name='service'),
    path('contact', contact, name='contact'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
