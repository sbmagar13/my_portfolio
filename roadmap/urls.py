from django.urls import path
from . import views

urlpatterns = [
    path('', views.roadmap, name='roadmap'),
    path('devops/', views.roadmap, name='devops-roadmap'),
    
]