from django.shortcuts import render
from django.views import generic

from task.models import Tag


def index(request):
    return render(request,'task/index.html')


class TagListView(generic.ListView):
    model = Tag
