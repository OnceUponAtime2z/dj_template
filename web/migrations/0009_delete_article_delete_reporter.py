# Generated by Django 4.0.2 on 2022-04-03 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_article_options_alter_reporter_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
    ]