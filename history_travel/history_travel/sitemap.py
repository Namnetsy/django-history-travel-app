from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from history_wiki.models import Post, Category

class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.published_date


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['index', 'about', 'search', 'categories']

    def location(self, item):
        return reverse(item)



SITEMAPS = {
	'postSitemap': PostSitemap,
	'staticViewSitemap': StaticViewSitemap,
}