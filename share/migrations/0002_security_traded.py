# Generated by Django 4.1.4 on 2022-12-13 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='security',
            name='traded',
            field=models.BooleanField(default=False),
        ),
    ]
