from django import forms

from authapp.models import MyUser


class SignUpForm(forms.ModelForm):
    class Meta:
        model = MyUser

        fields = ['email', 'phone']
