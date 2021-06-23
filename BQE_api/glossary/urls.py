from django.urls import path
from django.urls.conf import include
from .views.data_seeding_views import *
from .views.word_viewset import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'word', WordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('data', index, name='index'),
    path('seed_glossary', seed_glossary, name='seed_glossary'),
    path('delete_glossary', delete_glossary, name='delete_glossary'),
]
