# Generated by Django 4.1.2 on 2022-11-08 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructions', '0023_tag_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='owner',
        ),
    ]
