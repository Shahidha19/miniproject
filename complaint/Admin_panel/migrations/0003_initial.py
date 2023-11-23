# Generated by Django 4.2.5 on 2023-10-07 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin_panel', '0002_delete_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplaintSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.CharField(blank=True, max_length=100, null=True)),
                ('dept', models.CharField(blank=True, max_length=100, null=True)),
                ('complaint', models.CharField(blank=True, max_length=1000, null=True)),
                ('status', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
