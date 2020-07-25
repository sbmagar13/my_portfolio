from django.contrib import admin

from works.models import Work, Category_work
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class WorkAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', 'live', 'downloadOrView')
    list_display = ('title', 'slug', 'short_desciption', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content', 'live', 'download']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Work, WorkAdmin)
admin.site.register(Category_work)
