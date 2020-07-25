from django.urls import path
from . import views

urlpatterns = [
    path('', views.work_index, name='work_index'),
    path('<int:pk>/', views.work_detail, name='work_detail'),
    path('<category_work>/', views.work_category, name='work_category'),
    
]