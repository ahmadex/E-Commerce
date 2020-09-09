from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password1','password2']


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author','title','text']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['text']
