# Generated by Django 4.1.7 on 2023-04-07 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_remove_projectmodel_committee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='grademodel',
            name='subject',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.subjectmodel'),
        ),
    ]