from django import forms
from .models import Woodland


class WoodForm(forms.ModelForm):
    class Meta:
        model = Woodland
        fields = '__all__'
        labels = {
            'category': 'Category',
            'name': 'Name',
            'count': 'Count',
            'note': 'Note',
        }
        #help_texts = {
        #    'name': 'Name of the species',
        #}
        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-select',
                'aria-label': 'Category selection'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter species name'
            }),
            'count': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'placeholder': 'Enter count'
            }),
            'note': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,  # Makes the textarea bigger
                'placeholder': 'Additional notes'
            }),
        }
