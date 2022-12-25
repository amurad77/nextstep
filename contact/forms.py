from django import forms
from .models import Contact, Apply
from django.forms import ModelForm, Select



WHAT_IDEA = [
    ('1', 'Select an option'),
    ('2', 'Early idea'),
    ('3', 'Researched idea'),
    ('4', 'Mockups'),
    ]

HOURS = [
    ('1', 'Select an option'),
    ('2', '0-10'),
    ('3', '11-20'),
    ('4', '21-35'),
    ('5', '36+'),
    ]

PEOPLE = [
    ('1', 'Select an option'),
    ('2', '1'),
    ('3', '2'),
    ('4', '3'),
    ('5', '4+'),
    ]

INDUSTRIES = [
    ('1', 'Accouting / Finance / Legal'),
    ('2', 'Advertising / Marketing'),
    ]

AREAS = [
    ('1', 'Basic entrepreneurial training'),
    ('2', 'Improving my idea / strategy'),
    ('3', 'Building a network'),
    ('4', 'Finding a Co-Founder'),
    ('5', 'Building a team'),
    ('6', 'Product development'),
    ('7', 'Fundraising'),
    ('8', 'Marketing and Sales'),
    ('9', 'Internationalisation'),
    ('10', 'Strategic Partnership'),
    ]



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




class ApplyForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
                                    'placeholder': 'Your Name',
                                    'type': 'text'
                                }))
    surname = forms.CharField(widget=forms.TextInput(attrs={
                                    'placeholder': 'Your Surname',
                                    'type': 'text'
                                }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
                                    'placeholder': 'Your e-mail',
                                    'type': 'text'
                                }))
    number = forms.CharField(widget=forms.TextInput(attrs={
                                    'placeholder': 'Telephone',
                                    'type': 'text'
                                }))
    what_idea = forms.ChoiceField(choices=WHAT_IDEA)
    hours = forms.ChoiceField(choices=HOURS)

    idea = forms.CharField(widget=forms.TextInput(attrs={
                                    'placeholder': 'example: GameTech, TravelTech ....',
                                    'type': 'text'
                                }))
    describe = forms.CharField(widget=forms.Textarea(attrs={
                                    "placeholder": "Describe your startup",
                                    "rows":"5"
                                }))
    people = forms.ChoiceField(choices=PEOPLE)
    more_information = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    industries1 = forms.ChoiceField(choices=INDUSTRIES)
    industries2 = forms.ChoiceField(choices=INDUSTRIES)
    areas1 = forms.ChoiceField(choices=AREAS)
    areas2 = forms.ChoiceField(choices=AREAS)

    file = forms.FileField(widget=forms.FileInput())



    # class Meta:
    #     model = Apply
    #     fields = (
    #         'name',
    #         'surname',
    #         'email',
    #         'number',
    #         'what_idea',
    #         # 'project_name',
    #         # 'project_des',
    #         # 'team_members',
    #         # 'project_level',
    #         'file'
    #     )
        # file = forms.FileField(allow_empty_file=True)
        # widgets = {
        #     'name': forms.TextInput(attrs={
        #                             'placeholder': 'Your Name',
        #                             'type': 'text'
        #                         }),
        #     'surname': forms.TextInput(attrs={
        #                             'placeholder': 'Your Surname',
        #                             'type': 'text'
        #                         }),
        #     'email': forms.EmailInput(attrs={
        #                             'placeholder': 'Your e-mail',
        #                             'type': 'email'
        #                         }),
        #     'number': forms.TextInput(attrs={
        #                             'placeholder': 'Your Phone',
        #                             'type': 'tel'
        #                         }),
        #     'what_idea': Select(attrs={}),
        #     'file': forms.FileField(widget=forms.FileInput()),

        #     # 'project_name': forms.TextInput(attrs={
        #     #                         'placeholder': 'Project name',
        #     #                         'type': 'text'
        #     #                     }),
        #     # 'project_des': forms.Textarea(attrs={
        #     #                         'placeholder': 'Project description',
        #     #                     }),
        #     # 'team_members': forms.Textarea(attrs={
        #     #                         'placeholder': 'Team members',
        #     #                     }),
        #     # 'project_level': forms.Textarea(attrs={
        #     #                         'placeholder': 'What stage was the project currently in progress?',
        #     #                     }),
            
        # }