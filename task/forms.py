from django import forms
from .models import Tag, Task


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Name'
                },
            ),
        }
        labels = {
            "name": ""
        }


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            'content': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Content"
                },
            ),
            'deadline': forms.DateTimeInput(
                format="%Y-%m-%dT%H:%M",
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                    "placeholder": "Deadline"
                }
            )
        }
