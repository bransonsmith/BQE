from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('seed_glossary', seed_glossary, name='seed_glossary'),
]