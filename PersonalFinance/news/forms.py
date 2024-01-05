from .models import Articles
from django.forms import ModelForm, TextInput, Select, NumberInput, FloatField
from django import forms

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'subtitle', 'fulltext','date','time']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название кошелька',
            }),

            "fulltext": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название кошелька',
            }),
            "date": TextInput(attrs={

            }),
            "time": TextInput(attrs={

            }),

        }


