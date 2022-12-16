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

class Mentors(models.Model):
    # information
    name = models.CharField('Name Surname', max_length = 256)
    image = models.ImageField("Image", upload_to = 'media/mentors_images')
    work = models.CharField('Work name', max_length = 10000)
    linkedin_link = models.CharField('Linkedin link', max_length = 500)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Trainers(models.Model):
    # information
    name = models.CharField('Name Surname', max_length = 256)
    image = models.ImageField("Image", upload_to = 'media/trainers_images')
    work = models.CharField('Work name', max_length = 500)
    linkedin_link = models.CharField('Linkedin link', max_length = 500)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name