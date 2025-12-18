from django.urls import path
from .views import (
    TaskListView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    task_toggle,
)

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path("tags/", TagListView.as_view(), name='tag-list'),
    path("tags/create/", TagCreateView.as_view(), name='tag-create'),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name='tag-update'),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name='tag-delete'),
    path("task/<int:pk>/toggle/", task_toggle, name='task-toggle'),
]

app_name = 'task'