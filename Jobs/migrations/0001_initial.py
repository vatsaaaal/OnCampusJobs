# Generated by Django 4.0.1 on 2022-04-12 23:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_desc', models.CharField(blank=True, max_length=150)),
                ('description', models.TextField()),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('deadline', models.DateField()),
                ('location', models.CharField(max_length=100)),
                ('international', models.BooleanField()),
                ('eligibility', models.CharField(max_length=100)),
                ('major', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(max_length=50)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('major', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('fit', models.TextField()),
                ('resume', models.FileField(blank=True, upload_to='resume/')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Jobs.job')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
