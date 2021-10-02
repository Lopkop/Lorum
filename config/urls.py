from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forums/', include('forum.urls')),
    path('', include('pages.urls')),
]
