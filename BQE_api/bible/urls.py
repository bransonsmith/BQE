from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_chapters', views.delete_chapters, name='delete_chapters'),
    path('delete_testaments', views.delete_testaments, name='delete_testaments'),
]