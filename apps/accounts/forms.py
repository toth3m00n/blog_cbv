from django import forms
from django.contrib.auth.models import User

from apps.accounts.models import Profile

UPDATE_FORM_WIDGET = forms.TextInput(attrs={'class': 'form-control mb-1'})


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': UPDATE_FORM_WIDGET,
            'email': UPDATE_FORM_WIDGET,
            'first_name': UPDATE_FORM_WIDGET,
            'last_name': UPDATE_FORM_WIDGET
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError('Email адрес должен быть уникальным')
        if '@' not in email:
            raise forms.ValidationError('Неправильный email')
        return email


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('slug', 'birth_date', 'bio', 'avatar')
        widgets = {
            'slug': UPDATE_FORM_WIDGET,
            'birth_date': UPDATE_FORM_WIDGET,
            'bio': forms.Textarea(attrs={'rows': 5, "class": "form-control mb-1"}),
            'avatar': forms.FileInput(attrs={"class": "form-control mb-1"})
        }
