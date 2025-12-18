from django import forms
from .models import Tag


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