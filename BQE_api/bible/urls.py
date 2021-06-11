from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_chapters', views.delete_chapters, name='delete_chapters'),
    path('delete_testaments', views.delete_testaments, name='delete_testaments'),
    path('seed_testaments', views.seed_testaments, name='seed_testaments'),
    path('seed_books', views.seed_books, name='seed_books'),

]