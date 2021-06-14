from django.urls import path

from . import views

urlpatterns = [
    path('', homeView.as_view(),name='home')

]