from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('notes/', include('notes.urls')),
    path('games/', include('games.urls')),
    path('i18n/', include('django.conf.urls.i18n')),

]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += i18n_patterns(
    path('', include('main.urls')),
    path('notes/', include('notes.urls')),
    path('games/', include('games.urls')),
)