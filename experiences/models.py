from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField
import datetime


class Employment(models.Model):
    name = models.CharField(max_length=255, verbose_name="Company Name", blank=True)
    position = models.CharField(max_length=255, verbose_name="Position", blank=True)
    start_year = models.CharField(max_length=255, verbose_name="Start Year", blank=False, default="2020")
    start_month = models.CharField(max_length=255, verbose_name="Start Month", blank=False, default="January")
    end_year = models.CharField(max_length=255, verbose_name="End Year", blank=True)
    end_month = models.CharField(max_length=255, verbose_name="End Month", blank=True)
    current_status = models.BooleanField(default=False, verbose_name="Currently Working")
    end_date_value = models.CharField(max_length=255, verbose_name="End Date", blank=True)
    # time_period = models.CharField(max_length=255, verbose_name="Time Period", blank=True)
    description = MDTextField(verbose_name="Description", blank=True)
    town = models.CharField(max_length=255, verbose_name="City/Town", blank=True)
    url = models.URLField(max_length=255, verbose_name="URL", blank=True)

    def __str__(self):
        return self.name
    
    # def get_date(self):
    #     return self.start_date.date()

    # def get_date(self):
    #     return self.end_date.date()

    def save(self, *args, **kwargs):
        if self.current_status == True:
            self.end_date_value = 'Present'
        else:
            self.end_date_value = f"{self.end_month}, {self.end_year}"
        super().save(*args, **kwargs)


class Education(models.Model):
    name = models.CharField(max_length=255,verbose_name="School Name",blank=True)
    level = models.CharField(max_length=255, verbose_name="Level", blank=True)
    # time_period = models.CharField(max_length=255, verbose_name="Time Period", blank=True)
    start_date = models.DateTimeField(default=datetime.datetime.now)
    end_date = models.DateTimeField(default=datetime.datetime.now)
    description = MDTextField(verbose_name="Description", blank=True)
    town = models.CharField(max_length=255, verbose_name="City/Town", blank=True)
    url = models.URLField(max_length=255, verbose_name="URL", blank=True)

    def __str__(self):
        return self.name

    def get_date(self):
        return self.start_date.date()

    def get_date(self):
        return self.end_date.date()