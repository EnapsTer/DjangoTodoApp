from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='index'),
    path('createtask', views.TaskCreateView.as_view(), name='create_task')
]
