from django.urls import path
from web.views import About, Contact, index


urlpatterns = [
    path('', index, name='index'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact')
]