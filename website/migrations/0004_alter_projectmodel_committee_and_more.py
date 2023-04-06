# Generated by Django 4.1.7 on 2023-04-05 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_subjectmodel_scoremodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='committee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='committee', to='website.profmodel'),
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='consult',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consult', to='website.profmodel'),
        ),
    ]
