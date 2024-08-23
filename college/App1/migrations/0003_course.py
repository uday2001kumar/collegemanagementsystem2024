# Generated by Django 5.1 on 2024-08-17 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_alter_signinmodel_cpas_alter_signinmodel_pas_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('c_title', models.CharField(max_length=100)),
                ('c_id', models.IntegerField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=50, unique=True)),
                ('c_branch', models.CharField(max_length=50)),
                ('c_duration', models.CharField(max_length=10)),
                ('c_fee', models.DecimalField(decimal_places=4, max_digits=20)),
                ('c_hostal', models.CharField(choices=[('a', 'Available'), ('ua', 'Unavailable')], max_length=50)),
            ],
        ),
    ]
