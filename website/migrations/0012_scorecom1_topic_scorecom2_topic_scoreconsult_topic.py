# Generated by Django 4.1.7 on 2023-04-29 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_fileproject_score_delete_scoretopic'),
    ]

    operations = [
        migrations.AddField(
            model_name='scorecom1',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.topicproject'),
        ),
        migrations.AddField(
            model_name='scorecom2',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.topicproject'),
        ),
        migrations.AddField(
            model_name='scoreconsult',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.topicproject'),
        ),
    ]