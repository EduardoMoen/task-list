from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task.forms import TagForm
from task.models import Tag


def index(request):
    return render(request,'task/index.html')


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
