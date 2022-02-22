from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))