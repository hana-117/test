# Generated by Django 3.2.4 on 2023-11-21 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='contributor',
            new_name='owner',
        ),
    ]
