# Generated by Django 4.1.6 on 2023-03-26 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_alter_projectmodel_consult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='consult',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.profmodel'),
        ),
    ]
