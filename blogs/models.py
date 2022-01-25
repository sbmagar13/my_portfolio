from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.utils import timezone
from taggit.managers import TaggableManager

class PublishedManager(models.Manager):
    def ger_queryset(self):
        return super(PublishedManager, self).ger_queryset().filter(status=1)

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Published")
)


class Category_post(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    verbose_name_plural = 'categories'


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, unique_for_date='created_on')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    short_desciption = models.CharField(max_length=400, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    categories = models.ManyToManyField('Category_post', related_name='posts')
    visit_num = models.PositiveIntegerField(default=0)


    # Adding custom manager
    objects = models.Manager() # The default manager
    published = PublishedManager() # The Dahl Specfic manager

    tags = TaggableManager()

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.publish.year,
                                            self.publish.strftime('%m'),
                                            self.publish.strftime('%d'),
                                            self.slug
                                            ])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=200, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # manually deactivate inappropriate comments from admin site
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)
