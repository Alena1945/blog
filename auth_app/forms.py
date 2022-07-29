from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        print(self.cleaned_data)
        user = authenticate(**self.cleaned_data)
        if not user:
            raise forms.ValidationError('User not found')
        return {'user': user}
