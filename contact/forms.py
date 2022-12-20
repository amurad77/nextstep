from django import forms
from .models import Contact, Apply



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
                                    'placeholder': 'Your Name *',
                                    'type': 'text'
                                }),
            'email': forms.EmailInput(attrs={
                                    'placeholder': 'Your Email *',
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




class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = (
            'name_surname',
            'email',
            'number',
            'project_name',
            'project_des',
            'team_members',
            'project_level',
            # 'file'
        )
        # file = forms.FileField(allow_empty_file=True)
        widgets = {
            'name_surname': forms.TextInput(attrs={
                                    'placeholder': 'Your Name and Surname',
                                    'type': 'text'
                                }),
            'email': forms.EmailInput(attrs={
                                    'placeholder': 'Your e-mail',
                                    'type': 'email'
                                }),
            'number': forms.TextInput(attrs={
                                    'placeholder': 'Your Phone',
                                    'type': 'tel'
                                }),
            'project_name': forms.TextInput(attrs={
                                    'placeholder': 'Project name',
                                    'type': 'text'
                                }),
            'project_des': forms.Textarea(attrs={
                                    'placeholder': 'Project description',
                                }),
            'team_members': forms.Textarea(attrs={
                                    'placeholder': 'Team members',
                                }),
            'project_level': forms.Textarea(attrs={
                                    'placeholder': 'What stage was the project currently in progress?',
                                }),
            # 'file': forms.FileField(required=False),
        }