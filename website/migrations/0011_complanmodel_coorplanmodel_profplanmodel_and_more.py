# Generated by Django 4.1.5 on 2023-03-02 06:05

from django.db import migrations, models
import website.utils


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_stdmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComPlanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('list', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoorPlanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('list', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfPlanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('list', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StdPlanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('list', models.CharField(max_length=64, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=website.utils.file_path)),
            ],
        ),
    ]
