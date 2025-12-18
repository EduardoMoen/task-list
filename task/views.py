from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.http import require_POST

from task.forms import TagForm
from task.models import Tag , Task


@require_POST
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.concluded = not task.concluded
    task.save()
    return redirect('task:task-list')


class TaskListView(generic.ListView):
    model = Task


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('task:tag-list')


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('task:tag-list')


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy('task:tag-list')
