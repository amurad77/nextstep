# Generated by Django 4.1.4 on 2022-12-28 13:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcer',
            name='description',
            field=ckeditor.fields.RichTextField(default=1, max_length=10000, verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='events',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=10000, verbose_name='Description'),
        ),
    ]
