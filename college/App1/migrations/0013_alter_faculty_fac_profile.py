# Generated by Django 5.1.1 on 2024-11-06 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0012_alter_faculty_fac_exp_alter_faculty_fac_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='fac_profile',
            field=models.ImageField(upload_to=''),
        ),
    ]
