# Generated by Django 5.1.1 on 2024-09-11 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='name',
            new_name='first_name',
        ),
    ]
