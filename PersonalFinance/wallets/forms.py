from .models import Articles
from django.forms import ModelForm, TextInput, Select, NumberInput, FloatField
from django import forms

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'money', 'currency']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название кошелька',
            }),
            "money": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сумма',
                'step': 'any',
            }),
            "currency": Select(choices=[
                ('USD', 'USD'),
                ('BYN', 'BYN'),
                ('RUN', 'RUN'),
            ]),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['money'].widget.attrs['type'] = 'number'
