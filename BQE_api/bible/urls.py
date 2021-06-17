from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete', views.delete, name='delete'),
    path('seed', views.seed, name='seed'),
    path('seed_books', views.seed_books, name='seed_books'),
]