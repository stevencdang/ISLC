from django import forms
from website.models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration


