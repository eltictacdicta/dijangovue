from django.forms import ModelForm, Textarea
from .models import Comment, TypeContact


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
    SEX = (
        ('M','Masculino'),
        ('F','Femenino'),
        ('N','No binario')
    )
    #name = forms.CharField(label="Nombre", required=True, disabled=False, help_text="Aquí va tu nombre", max_length=10, min_length=2)
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}) ,label="Nombre", validators=[MinLengthValidator(2, message="Muy corto! (minimo %(limit_value)d) actual %(show_value)d")])
    surname = forms.CharField(label="Apellido", required=False , max_length=10, min_length=2)
    #phone = forms.RegexField(label='Telefono', regex='\(\w{3}\)\w{3}-\w{4}')
    phone = forms.CharField(label='Telefono',initial="999999999")
    date_birth = forms.DateField(widget=forms.DateInput(),label='Fecha de nacimiento',initial="9/7/1981")
    email = forms.EmailField(label="Correo",initial="loquesea@gmial.com")
    #mail = forms.CharField(label="Email", validators=[EmailValidator("No es un email válido")])
    document = forms.FileField(label="Documento",required=False)
    terms = forms.BooleanField(label="Condiciones de servicio")
    #type_contact = forms.ChoiceField(label="Tipo de contacto", choices=CHOICE, initial=2)
    type_contact = forms.ModelChoiceField(label="Tipo de contacto", queryset=TypeContact.objects.all())
    sex = forms.ChoiceField(label="Sexo", choices=SEX, initial="N")
