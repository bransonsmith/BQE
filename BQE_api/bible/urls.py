from django.urls import path

from . import views

urlpatterns = [
    path('delete_bible_data', views.delete_bible_data, name='delete_bible_data'),
    path('delete_testaments', views.delete_testaments, name='delete_testaments'),
    path('seed_bible_data', views.seed_bible_data, name='seed_bible_data'),
    path('seed_books', views.seed_books, name='seed_books'),
]