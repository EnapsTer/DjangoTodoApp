from django.shortcuts import render
from django.views import generic
from .models import Task, Tag

# Create your views here.


class TaskListView(generic.ListView):
    model = Task
    template_name = 'todoapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = 'todoapp/task_form.html'
    fields = ['title', 'about', 'date_of_completion']

