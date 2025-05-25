from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)

class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=('title','content','category','status','published_date')