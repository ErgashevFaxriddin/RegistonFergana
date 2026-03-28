from django import forms
from .models import Application, Jobs


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

    # ixtiyoriy validatsiya (xohlasang)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Application.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu email allaqachon ishlatilgan!")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if Application.objects.filter(phone=phone).exists():
            raise forms.ValidationError("Bu raqam allaqachon ishlatilgan!")
        return phone