# Generated by Django 3.0.2 on 2020-02-21 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('u_app', '0001_starting_over'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='password2',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
