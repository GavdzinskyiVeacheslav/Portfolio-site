from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('notes/', include('notes.urls')),
    path('games/', include('games.urls')),
]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)