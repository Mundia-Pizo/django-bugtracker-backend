# Generated by Django 3.0.6 on 2020-06-03 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_remove_tracker_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracker',
            name='resolved',
        ),
    ]