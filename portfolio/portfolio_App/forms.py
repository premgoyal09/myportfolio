from django import forms
from .models import Contact

class SignupForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        } 