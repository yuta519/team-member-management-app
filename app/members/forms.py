from django import forms
from django.forms import RadioSelect, TextInput

from members.models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["first_name", "last_name", "phone", "email", "role"]
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Enter your first name', 'class': 'form-input'}),
            'last_name': TextInput(attrs={'placeholder': 'Enter your last name', 'class': 'form-input'}),
            'phone': TextInput(attrs={'placeholder': 'Enter your phone number', 'class': 'form-input'}),
            'email': TextInput(attrs={'placeholder': 'Enter your email', 'class': 'form-input'}),
            'role': RadioSelect(),
        }
