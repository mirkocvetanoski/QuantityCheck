# Generated by Django 4.1.2 on 2022-11-30 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructions', '0043_remove_earth_measure_unit_alter_tag_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MeasureUnit',
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
