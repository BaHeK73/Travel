from django.contrib import admin
from django.urls import path, include
from Travel.apps.core.views import HomeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('hotels/', include('Travel.apps.hotels.urls', namespace='hotels')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 