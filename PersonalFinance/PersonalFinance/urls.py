from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('profile/', include('django.contrib.auth.urls')),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
