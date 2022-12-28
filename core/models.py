from django.db import models
# from tinymce import models as tinymce_models
from django.utils.text import slugify
from django.urls import reverse
# from colorfield.fields import ColorField

from ckeditor.fields import RichTextField


# Create your models here.
class Events(models.Model):
    # information
    title = models.CharField('Title', max_length = 256)
    cover_image = models.ImageField("Cover Image", upload_to = 'events_cover_images')
    des_image = models.ImageField("Des Image", upload_to = 'events_des_images')
    # description = tinymce_models.HTMLField('Description', max_length = 10000)
    description = RichTextField('Description', max_length = 10000)
    slug = models.SlugField('Slug', max_length = 256, unique = True, editable = False)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('events_details', kwargs = {'slug': self.slug})

    def get_uniqe_slug(self):
        slug = slugify(self.title.replace('ə', 'e'))
        unique_slug = slug
        counter = 1
        while Events.objects.filter(slug = unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug
    
    def save(self, *args, **kwargs):
        self.slug = self.get_uniqe_slug()
        return super(Events, self).save(*args, **kwargs)

class Announcer(models.Model):
    # information
    name = models.CharField('Name Surname', max_length = 256)
    image = models.ImageField("Image", upload_to = 'announcer_images')
    work = models.CharField('Work name', max_length = 10000)
    # description = tinymce_models.HTMLField('Description', max_length = 10000)
    description = RichTextField('Description', max_length = 10000)
    linkedin_link = models.CharField('Linkedin link', max_length = 500)

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