# Generated by Django 3.0.2 on 2020-02-04 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('u_app', '0003_auto_20200204_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='registration_date',
            field=models.DateTimeField(),
        ),
    ]
