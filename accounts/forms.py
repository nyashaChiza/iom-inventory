from django import forms
from accounts.models import CustomUser

from django import forms
from .models import CustomUser

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'role']  # Include any additional fields you need

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap 'form-control' class to each field
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            user.save()
        return user