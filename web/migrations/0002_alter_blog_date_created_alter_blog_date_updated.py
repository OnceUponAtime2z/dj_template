# Generated by Django 4.0.2 on 2022-04-01 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]