from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('froala_editor/', include('froala_editor.urls')),
    path('', include('history_wiki.urls')),
    path('account/', include('auth_wiki.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
