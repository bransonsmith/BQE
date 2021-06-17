from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('bible/', include('bible.urls')),
    path('glossary/', include('glossary.urls')),
    path('admin/', admin.site.urls),
]
