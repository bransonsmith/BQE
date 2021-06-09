from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('import_bible_data/', include('bible.urls')),
    path('admin/', admin.site.urls),
]
