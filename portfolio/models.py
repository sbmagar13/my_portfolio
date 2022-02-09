from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=200, blank=True)
    subject = models.CharField(max_length=80)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
   

    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)

    def __str__(self):
        return 'Contact by {}'.format(self.name)


class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'
    
    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="skills")
    is_key_skill = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


class Experience(models.Model):
    class Meta:
        verbose_name_plural = "Skills"
        verbose_name = "Skill"

    company = models.CharField(max_length=80, blank=False, null=True)
    role = models.CharField(max_length=80, blank=True, null=True)
    date_joined = models.DateTimeField(blank=False, null=True)
    # description 

    