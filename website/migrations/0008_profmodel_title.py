# Generated by Django 4.1.6 on 2023-02-15 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_profmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='profmodel',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
