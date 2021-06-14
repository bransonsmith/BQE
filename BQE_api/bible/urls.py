from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_bible_data', views.delete_bible_data, name='delete_bible_data'),
    path('seed_bible_data', views.seed_bible_data, name='seed_bible_data'),

]