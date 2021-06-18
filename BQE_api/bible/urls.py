from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_bible', views.delete_bible, name='delete_bible'),
    path('seed_bible', views.seed_bible, name='seed_bible'),
    path('seed_books', views.seed_books, name='seed_books'),
]