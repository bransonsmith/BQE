from django import urls
from django.urls import path
from django.urls.conf import include
from .views import *
from glossary.api.urls import *

app_name = 'glossary'


urlpatterns = [

    path('', index, name='index'),
    path('seed_glossary', seed_glossary, name='seed_glossary'),
    path('delete_glossary', delete_glossary, name='delete_glossary'),

    #REST FRAMEWORK
    path('api/', include('glossary.api.urls','api'))
    
]