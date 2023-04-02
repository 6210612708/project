# Generated by Django 4.1.6 on 2023-04-01 10:01

import annoying.fields
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_docproject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docproject',
            name='id',
        ),
        migrations.AlterField(
            model_name='docproject',
            name='project',
            field=annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='website.projectmodel'),
        ),
    ]
