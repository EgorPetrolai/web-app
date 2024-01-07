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
                'placeholder': 'Заголовок',
            }),
            "subtitle": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание',
            }),

            "fulltext": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Текст новости',
            }),
            "date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата',
            }),
            "time": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время',
            }),

        }


