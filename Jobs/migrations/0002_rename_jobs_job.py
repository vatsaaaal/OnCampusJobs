# Generated by Django 4.0.1 on 2022-02-03 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Jobs',
            new_name='Job',
        ),
    ]