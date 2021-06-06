from django.forms import *
from .models import *


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': ' Name'
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'content': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Content'
            }),
        }





    # name = forms.CharField(label='Имя', max_length=255)
    # email = forms.EmailField(label='Email')
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
