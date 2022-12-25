from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
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


class Contact(models.Model):
    
    # information
    name = models.CharField('Your Name', max_length = 256)
    email = models.EmailField('Your Email', max_length = 50)
    number = models.CharField('Your Phone', max_length = 20)
    message = models.TextField('Message', max_length = 5000)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.name

class Apply(models.Model):
    
    # information
    name = models.CharField('First name', max_length = 256)
    surname = models.CharField('Last name', max_length = 256)
    email = models.EmailField('Your e-mail', max_length = 60)
    number = models.CharField('Your Phone', max_length = 30)
    what_idea = models.CharField('What state is your idea', choices = WHAT_IDEA, default = 'Select an option', max_length = 256)
    idea = models.CharField('What field is your idea / product / service in?', max_length = 530)
    describe = models.TextField('Describe your startup', max_length = 30000)
    hours = models.CharField('How many hours', choices = HOURS, default = 'Select an option', max_length = 1000)
    people = models.CharField('How many people', choices = PEOPLE, default = 'Select an option', max_length = 1000)
    more_information = models.TextField('More information about team members', max_length = 100)
    industries1 = models.CharField('Two industries that best describe the business you are building (Primary)', choices = INDUSTRIES, max_length = 1000)
    industries2 = models.CharField('Two industries that best describe the business you are building (Secondary)', choices = INDUSTRIES, max_length = 1000)
    areas1 = models.CharField('Select the two areas where you most need help building a business (Primary)', choices = AREAS, max_length = 1000)
    areas2 = models.CharField('Select the two areas where you most need help building a business (Secondary)', choices = AREAS, max_length = 1000)

    # project_name = models.CharField('Project name', max_length = 256)
    # project_des = models.TextField('Project description', max_length = 20000)
    # team_members = models.TextField('Team members', max_length = 10000)
    # project_level = models.TextField('What stage was...', max_length = 15000)
    file = models.FileField('File', upload_to='file', null=False, blank=False)


    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.name