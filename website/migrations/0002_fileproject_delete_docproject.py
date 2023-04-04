# Generated by Django 4.1.6 on 2023-04-04 09:13

from django.db import migrations, models
import django.db.models.deletion
import website.utils


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fileproject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(choices=[('proposal', 'proposal'), ('preliminary', 'preliminary'), ('progress1', 'progress1'), ('progress2', 'progress2'), ('draftthesis', 'draftthesis'), ('finalthesis', 'finalthesis')], max_length=200, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=website.utils.file_path)),
                ('date', models.DateTimeField(null=True)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.projectmodel')),
            ],
        ),
        migrations.DeleteModel(
            name='Docproject',
        ),
    ]
