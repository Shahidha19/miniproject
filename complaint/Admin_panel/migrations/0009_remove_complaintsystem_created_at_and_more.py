# Generated by Django 4.2.5 on 2023-10-21 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_panel', '0008_complaintsystem_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaintsystem',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='complaintsystem',
            name='updated_at',
        ),
    ]
