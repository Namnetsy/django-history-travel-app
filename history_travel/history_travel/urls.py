from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap

from .sitemap import PostSitemap
from .sitemap import SITEMAPS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('froala_editor/', include('froala_editor.urls')),
    path('', include('history_wiki.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': SITEMAPS},
    	  name='django.contrib.sitemaps.views.sitemap')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
