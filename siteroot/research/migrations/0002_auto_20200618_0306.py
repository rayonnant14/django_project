# Generated by Django 3.0.7 on 2020-06-18 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='researcher',
            old_name='title',
            new_name='author',
        ),
    ]
