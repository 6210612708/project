# Generated by Django 4.1.6 on 2023-02-08 09:06

from django.db import migrations, models
import website.utils


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_docmodel_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docmodel',
            name='file',
            field=models.FileField(null=True, upload_to=website.utils.file_path),
        ),
    ]
