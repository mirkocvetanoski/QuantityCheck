# Generated by Django 4.1.2 on 2022-11-18 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_options_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['is_read', 'created']},
        ),
    ]
