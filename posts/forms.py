from django import forms

from posts.models import Article, Profile


class ArticleForm(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': "Say something..."}))

    class Meta:
        model = Article
        fields = ('title','body', 'image',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = '__all__'
