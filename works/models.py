from django.db import models

from django.contrib.auth.models import User


# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Category_work(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    verbose_name_plural = 'categories'


class Work(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='work_posts')
    updated_on = models.DateTimeField(auto_now= True)
    short_desciption = models.CharField(max_length=400, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    content = models.TextField( blank=True, null=True)
    live = models.TextField( blank=True, null=True)
    downloadOrView = models.TextField( blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    categories = models.ManyToManyField('Category_work', related_name='works')
    visit_num = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
