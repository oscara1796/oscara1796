# Generated by Django 3.2.5 on 2021-07-25 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]