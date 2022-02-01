from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('students/', include('students.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
