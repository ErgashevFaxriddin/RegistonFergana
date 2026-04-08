from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'email', 'phone', 'job']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Ismingiz'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Telefon raqam'
            }),
            'job': forms.Select(attrs={
                'class': 'w-full p-2 border rounded'
            }),
        }