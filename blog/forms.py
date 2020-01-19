from .models import Comment, Contact
from django import forms
from django.forms import Textarea


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'body')
        widgets = {
            'body': Textarea(attrs={'rows':40, 'cols':20}),
        }
