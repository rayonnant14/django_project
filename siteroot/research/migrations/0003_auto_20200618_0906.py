# Generated by Django 3.0.7 on 2020-06-18 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0002_auto_20200618_0306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='researcher',
            new_name='post',
        ),
    ]
