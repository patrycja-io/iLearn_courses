# Generated by Django 3.0.7 on 2020-08-09 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_course_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
