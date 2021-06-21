from django import urls
from django.urls import path
from django.urls.conf import include

from rest_framework import routers, serializers, viewsets

from .views import *

app_name = 'glossary'


router = routers.DefaultRouter()
router.register(r'word', WordViewSet)
router.register(r'answer', AnswerViewSet)



urlpatterns = [
    path('', include(router.urls)),
    

]