# Generated by Django 4.0.2 on 2022-04-03 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('web', '0009_delete_article_delete_reporter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categorys',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_code', models.CharField(max_length=13)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=22)),
                ('subject_name_th', models.CharField(max_length=255)),
                ('subject_name_en', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.category')),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
            },
        ),
    ]
