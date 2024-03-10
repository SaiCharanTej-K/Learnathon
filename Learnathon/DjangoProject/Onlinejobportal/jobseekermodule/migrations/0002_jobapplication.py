# Generated by Django 5.0.1 on 2024-03-09 22:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employermodule', '0001_initial'),
        ('jobseekermodule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('resume', models.FileField(upload_to='resume/')),
                ('cover_letter', models.TextField()),
                ('job_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employermodule.jobdetails')),
            ],
        ),
    ]