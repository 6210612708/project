# Generated by Django 4.1.7 on 2023-05-02 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_remove_scorecom1_sc7_remove_scorecom1_sc8_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stdplanmodel',
            name='file',
        ),
        migrations.AlterField(
            model_name='docmodel',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
