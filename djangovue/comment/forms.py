from django.forms import ModelForm, Textarea
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={
                'class':'form-input'
            })
        }
    def save(self, commit=True):
        instance = super(CommentForm, self).save(commit=commit)
        if(commit):
            instance.save()

from django import forms 

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, disabled=True, help_text="Aquí va tu nombre", max_length=10, min_length=2)
