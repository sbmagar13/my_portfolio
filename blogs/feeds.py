from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from blogs.models import Post


class LatestPostsFeeds(Feed):
    title = "Sagar's blog"
    link = '/blogs/'
    description = 'New posts of my blogs.'

    def items(self):
        return Post.objects.order_by('-publish')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)