from django.db import models
from mdeditor.fields import MDTextField

# from roadmap.views import roadmap

class Roadmap(models.Model):
    roadmap_name = models.CharField(verbose_name="Roadmap Name", max_length=40)

class RoadmapTopic(models.Model):
    topic_name = models.CharField(verbose_name="Topic Name", max_length=100)
    roadmap_name = models.ForeignKey(Roadmap, related_name='roadmap', on_delete=models.CASCADE)
    topic_description = MDTextField(verbose_name="Description", blank=True)
    image = models.ImageField(upload_to='images/')
    priority = models.IntegerField(verbose_name="Priority Value")

    def __str__(self):
        return self.topic_name