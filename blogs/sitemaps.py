from django.contrib.sitemaps import Sitemap

from blogs.models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()


    def lastmod(self, obj):
        return obj.publish