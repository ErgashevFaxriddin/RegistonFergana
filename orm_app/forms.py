from django import forms
from .models import Application, Customer


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = "__all__"


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"