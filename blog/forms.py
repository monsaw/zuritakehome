from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

        widgets = {
        'title':forms.TextInput(attrs = {'class' : 'form-control'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','body')
