from django import forms
from .models import User, ArticlesModel
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
         'class':'form-control'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
         'class':'form-control'
    }))
    role = forms.ChoiceField(choices=User.role_choices,widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
         'class':'form-control'
    }))
    class Meta:
        model = User
        fields = [ 'email', 'password', 'role', 'username']



class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control'
            }
        )
    )

class ArticleCreationForm(forms.ModelForm):
    article_title = forms.CharField(widget=forms.TextInput(attrs={
         'class':'form-control'
    }))
    subtitle = forms.CharField(widget=forms.TextInput(attrs={
         'class':'form-control'
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))
    file_url = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control',
        'accept': 'image/*'
    }))
    class Meta:
        model = ArticlesModel
        fields = [ 'article_title', 'subtitle', 'description', "file_url"]

class ArticleEditForm(forms.ModelForm):
    article_title = forms.CharField(widget=forms.TextInput(attrs={
         'class':'form-control'
    }))
    subtitle = forms.CharField(widget=forms.TextInput(attrs={
         'class':'form-control'
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))
    file_url = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control',
        'accept': 'image/*'
    }))
    class Meta:
        model = ArticlesModel
        fields = [ 'article_title', 'subtitle', 'description', "file_url"]