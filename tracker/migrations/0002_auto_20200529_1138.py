# Generated by Django 3.0.6 on 2020-05-29 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracker',
            old_name='Project',
            new_name='project',
        ),
    ]
