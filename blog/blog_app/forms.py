from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm
)

from django import forms
from django.contrib.auth.models import User
from .models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'short_description', 'full_description', 'preview', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control'}),
            'full_description': forms.TextInput(attrs={'class': 'form-control'}),
            'preview': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = User
        fields = ('username', 'password')

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(
                attrs={'class': 'form-control'}
            ),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(
                attrs={'class': 'form-control'}
            )
        }