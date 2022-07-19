from django import forms
from django.contrib import admin
from django.shortcuts import get_object_or_404
from .models import Employment, Education


class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    search_fields = ['name']
    exclude = ('end_date_value', 'created_on')


    

class EducationAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    search_fields = ['name']


admin.site.register(Employment, EmploymentAdmin)
admin.site.register(Education, EducationAdmin)