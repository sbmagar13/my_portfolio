from django.contrib import admin
from .models import Employment, Education


class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    search_fields = ['name']


class EducationAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    search_fields = ['name']


admin.site.register(Employment, EmploymentAdmin)
admin.site.register(Education, EducationAdmin)