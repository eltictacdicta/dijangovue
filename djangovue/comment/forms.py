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
from django.core.validators import MinLengthValidator,EmailValidator

class ContactForm(forms.Form):
    #name = forms.CharField(label="Nombre", required=True, disabled=False, help_text="Aquí va tu nombre", max_length=10, min_length=2)
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}) ,label="Nombre", validators=[MinLengthValidator(2, message="Muy corto! (minimo %(limit_value)d) actual %(show_value)d")])
    surname = forms.CharField(label="Apellido", required=False , max_length=10, min_length=2)
    #phone = forms.RegexField(label='Telefono', regex='\(\w{3}\)\w{3}-\w{4}')
    phone = forms.CharField(label='Telefono')
    date_birth = forms.DateField(widget=forms.DateInput(),label='Fecha de nacimiento')
    email = forms.EmailField(label="Correo")
    #mail = forms.CharField(label="Email", validators=[EmailValidator("No es un email válido")])
    document = forms.FileField(label="Documento")
    terms = forms.BooleanField(label="Condiciones de servicio")
