from django import forms
from .models import Contact



class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'number',
            'message',
        )
        widgets = {
            'name': forms.TextInput(attrs={
                                    'placeholder': 'Your Name*',
                                    'type': 'text'
                                }),
            'email': forms.EmailInput(attrs={
                                    'placeholder': 'Your Email*',
                                    'type': 'email'
                                }),
            'number': forms.TextInput(attrs={
                                    'placeholder': 'Your Phone',
                                    'type': 'tel'
                                }),
            'message': forms.Textarea(attrs={
                                    'placeholder': 'Message',
                                })
        }