# Generated by Django 5.1.7 on 2025-03-19 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherdata', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weatherdata',
            old_name='wind_directory',
            new_name='wind_direction',
        ),
    ]
