"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    
    # 다음 두 줄은 'Individual Topic Pages' 코딩에서 필요
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]