from django import forms
from django.forms import ModelForm
from .models import Profile, Article, Tag


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['age', 'gender', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Коротко про себе...'}),
        }
        labels = {
            'age': 'Вік',
            'gender': 'Стать',
            'bio': 'Про себе',
        }


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        exclude = ['author']
        widgets = {
            'published': forms.DateInput(attrs={'type': 'date'}),
            'body': forms.Textarea(attrs={'rows': 8}),
        }


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        labels = {'name': 'Тег'}
