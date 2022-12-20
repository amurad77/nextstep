from django.db import models

# Create your models here.


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
    name_surname = models.CharField('Your Name and Surname', max_length = 256)
    email = models.EmailField('Your e-mail', max_length = 60)
    number = models.CharField('Your Phone', max_length = 30)
    project_name = models.CharField('Project name', max_length = 256)
    project_des = models.TextField('Project description', max_length = 20000)
    team_members = models.TextField('Team members', max_length = 10000)
    project_level = models.TextField('What stage was...', max_length = 15000)
    file = models.FileField('File', upload_to='file', null=False, blank=False)


    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.name_surname