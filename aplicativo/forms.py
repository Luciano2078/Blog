from django.forms import fields
from .formulario import Comment

from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

        
