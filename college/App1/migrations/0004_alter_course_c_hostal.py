# Generated by Django 5.1 on 2024-08-17 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='c_hostal',
            field=models.CharField(choices=[('Available', 'a'), ('Unavailable', 'ua')], max_length=50),
        ),
    ]
