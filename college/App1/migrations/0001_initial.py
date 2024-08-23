# Generated by Django 5.0.8 on 2024-08-07 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SigninModel',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('pas', models.CharField(max_length=30)),
                ('cpas', models.CharField(max_length=30)),
            ],
        ),
    ]