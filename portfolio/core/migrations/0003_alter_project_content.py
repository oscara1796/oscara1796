# Generated by Django 3.2.5 on 2021-07-25 19:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_project_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
