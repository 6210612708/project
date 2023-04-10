# Generated by Django 4.1.6 on 2023-04-10 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_remove_projectmodel_committee_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scoremodel',
            name='sc1',
        ),
        migrations.RemoveField(
            model_name='scoremodel',
            name='sc2',
        ),
        migrations.RemoveField(
            model_name='scoremodel',
            name='sc3',
        ),
        migrations.RemoveField(
            model_name='scoremodel',
            name='sc4',
        ),
        migrations.RemoveField(
            model_name='scoremodel',
            name='sc5',
        ),
        migrations.RemoveField(
            model_name='scoremodel',
            name='sc6',
        ),
        migrations.RemoveField(
            model_name='scoremodel',
            name='sc7',
        ),
        migrations.RemoveField(
            model_name='scoremodel',
            name='sc8',
        ),
        migrations.CreateModel(
            name='ScoreConsult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sc1', models.IntegerField(blank=True, null=True)),
                ('sc2', models.IntegerField(blank=True, null=True)),
                ('sc3', models.IntegerField(blank=True, null=True)),
                ('sc4', models.IntegerField(blank=True, null=True)),
                ('sc5', models.IntegerField(blank=True, null=True)),
                ('sc6', models.IntegerField(blank=True, null=True)),
                ('sc7', models.IntegerField(blank=True, null=True)),
                ('sc8', models.IntegerField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('consult', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.profmodel')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.projectmodel')),
                ('std1', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='std1con', to='website.stdmodel')),
                ('std2', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='std2con', to='website.stdmodel')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.subjectmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ScoreCom2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sc1', models.IntegerField(blank=True, null=True)),
                ('sc2', models.IntegerField(blank=True, null=True)),
                ('sc3', models.IntegerField(blank=True, null=True)),
                ('sc4', models.IntegerField(blank=True, null=True)),
                ('sc5', models.IntegerField(blank=True, null=True)),
                ('sc6', models.IntegerField(blank=True, null=True)),
                ('sc7', models.IntegerField(blank=True, null=True)),
                ('sc8', models.IntegerField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('consult', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.profmodel')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.projectmodel')),
                ('std1', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='std1sc2', to='website.stdmodel')),
                ('std2', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='std2sc2', to='website.stdmodel')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.subjectmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ScoreCom1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sc1', models.IntegerField(blank=True, null=True)),
                ('sc2', models.IntegerField(blank=True, null=True)),
                ('sc3', models.IntegerField(blank=True, null=True)),
                ('sc4', models.IntegerField(blank=True, null=True)),
                ('sc5', models.IntegerField(blank=True, null=True)),
                ('sc6', models.IntegerField(blank=True, null=True)),
                ('sc7', models.IntegerField(blank=True, null=True)),
                ('sc8', models.IntegerField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('consult', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.profmodel')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.projectmodel')),
                ('std1', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='std1sc1', to='website.stdmodel')),
                ('std2', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='std2sc1', to='website.stdmodel')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.subjectmodel')),
            ],
        ),
        migrations.AddField(
            model_name='scoremodel',
            name='com1sc',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.scorecom1'),
        ),
        migrations.AddField(
            model_name='scoremodel',
            name='com2sc',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.scorecom2'),
        ),
        migrations.AddField(
            model_name='scoremodel',
            name='consc',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.scoreconsult'),
        ),
    ]
