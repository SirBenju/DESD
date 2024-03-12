from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['FirstName', 'LastName', 'Email', 'Password', 'UserRole', 'Address', 'PhoneNumber']
        widgets = {
            'Password': forms.PasswordInput(),
        }
