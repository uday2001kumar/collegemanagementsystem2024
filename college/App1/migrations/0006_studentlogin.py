# Generated by Django 5.1 on 2024-08-17 11:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0005_alter_course_c_hostal'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentLogin',
            fields=[
                ('s_roll', models.IntegerField(primary_key=True, serialize=False)),
                ('s_dob', models.DateField()),
                ('s_name', models.CharField(max_length=100)),
                ('s_branch', models.CharField(max_length=50)),
                ('s_year', models.CharField(max_length=10)),
                ('s_address', models.TextField()),
                ('s_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.course')),
            ],
        ),
    ]
