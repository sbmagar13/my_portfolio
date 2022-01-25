from django.urls import path, re_path
from . import views

# app_name = 'blogs'

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    # path('<slug:post>/', views.blog_detail, name='blog_detail'),
    path('<category_post>/', views.blog_category, name='blog_category'),

    re_path(r'^tag/(?P<tag_slug>[-\w]+)/$', views.blog_index, name='blog_index_list_by_tag'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.blog_detail, name='blog_detail')

]
