# Generated by Django 4.1.5 on 2023-04-24 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_scorecom1_std1_alter_scorecom1_std2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodel',
            name='major',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='scoremodel',
            name='major',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]