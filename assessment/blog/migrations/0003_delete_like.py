# Generated by Django 4.0 on 2022-01-17 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_like'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
    ]
