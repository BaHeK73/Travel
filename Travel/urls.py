from django.contrib import admin
from django.urls import path, include
# from Travel.apps.core.views import HomeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Travel.apps.core.urls')),
    path('hotels/', include('Travel.apps.hotels.urls', namespace='hotels')),
    path('users/', include('Travel.apps.users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 