# Generated by Django 3.0.6 on 2020-06-03 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20200529_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracker',
            name='project',
        ),
    ]