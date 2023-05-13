# Generated by Django 4.1.7 on 2023-05-13 07:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import website.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CoorPlanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('list', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, null=True)),
                ('file', models.FileField(null=True, upload_to='')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('list', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, null=True)),
                ('detail', models.CharField(max_length=500, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ProfModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('fname', models.CharField(max_length=100, null=True)),
                ('lname', models.CharField(max_length=100, null=True)),
                ('major', models.CharField(choices=[('ไฟฟ้า', 'ไฟฟ้า'), ('คอมพิวเตอร์', 'คอมพิวเตอร์')], max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfPlanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('list', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thainame', models.CharField(max_length=100, null=True)),
                ('engname', models.CharField(max_length=100, null=True)),
                ('detail', models.CharField(max_length=500, null=True)),
                ('status', models.CharField(choices=[('ยังไม่มีนักศึกษาลงทะเบียน', 'ยังไม่มีนักศึกษาลงทะเบียน'), ('รอการอนุมัติ', 'รอการอนุมัติ'), ('อนุมัติ', 'อนุมัติ')], default='ยังไม่มีนักศึกษาลงทะเบียน', max_length=200, null=True)),
                ('major', models.CharField(blank=True, max_length=100, null=True)),
                ('committee1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='committee1', to='website.profmodel')),
                ('committee2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='committee2', to='website.profmodel')),
                ('consult', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consult', to='website.profmodel')),
            ],
        ),
        migrations.CreateModel(
            name='StdPlanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('list', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, null=True)),
                ('year', models.IntegerField(default=website.models.SubjectModel.current_year, null=True)),
                ('startterm', models.DateField(null=True)),
                ('endterm', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topicproject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200, null=True)),
                ('datedue', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StdModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdid', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(choices=[('นาย', 'นาย'), ('นางสาว', 'นางสาว')], max_length=100, null=True)),
                ('fname', models.CharField(max_length=100, null=True)),
                ('lname', models.CharField(max_length=100, null=True)),
                ('major', models.CharField(choices=[('ไฟฟ้า', 'ไฟฟ้า'), ('คอมพิวเตอร์', 'คอมพิวเตอร์')], max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScoreModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(blank=True, max_length=100, null=True)),
                ('sccon', models.IntegerField(blank=True, null=True)),
                ('sccom1', models.IntegerField(blank=True, null=True)),
                ('sccom2', models.IntegerField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('grade', models.CharField(blank=True, max_length=10, null=True)),
                ('committee1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='com1', to='website.profmodel')),
                ('committee2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='com2', to='website.profmodel')),
                ('consult', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.profmodel')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.projectmodel')),
                ('std1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='std1', to='website.stdmodel')),
                ('std2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='std2', to='website.stdmodel')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.subjectmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ScoreConsult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sc1', models.IntegerField(blank=True, default=0, null=True)),
                ('sc2', models.IntegerField(blank=True, default=0, null=True)),
                ('sc3', models.IntegerField(blank=True, default=0, null=True)),
                ('sc4', models.IntegerField(blank=True, default=0, null=True)),
                ('sc5', models.IntegerField(blank=True, default=0, null=True)),
                ('sc6', models.IntegerField(blank=True, default=0, null=True)),
                ('sc7', models.IntegerField(blank=True, default=0, null=True)),
                ('sc8', models.IntegerField(blank=True, default=0, null=True)),
                ('score', models.IntegerField(blank=True, default=0, null=True)),
                ('consult', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.profmodel')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.projectmodel')),
                ('std1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='std1con', to='website.stdmodel')),
                ('std2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='std2con', to='website.stdmodel')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.subjectmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ScoreCom2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sc1', models.IntegerField(blank=True, default=0, null=True)),
                ('sc2', models.IntegerField(blank=True, default=0, null=True)),
                ('sc3', models.IntegerField(blank=True, default=0, null=True)),
                ('sc4', models.IntegerField(blank=True, default=0, null=True)),
                ('sc5', models.IntegerField(blank=True, default=0, null=True)),
                ('sc6', models.IntegerField(blank=True, default=0, null=True)),
                ('score', models.IntegerField(blank=True, default=0, null=True)),
                ('consult', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.profmodel')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.projectmodel')),
                ('std1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='std1sc2', to='website.stdmodel')),
                ('std2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='std2sc2', to='website.stdmodel')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.subjectmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ScoreCom1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sc1', models.IntegerField(blank=True, default=0, null=True)),
                ('sc2', models.IntegerField(blank=True, default=0, null=True)),
                ('sc3', models.IntegerField(blank=True, default=0, null=True)),
                ('sc4', models.IntegerField(blank=True, default=0, null=True)),
                ('sc5', models.IntegerField(blank=True, default=0, null=True)),
                ('sc6', models.IntegerField(blank=True, default=0, null=True)),
                ('score', models.IntegerField(blank=True, default=0, null=True)),
                ('consult', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.profmodel')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.projectmodel')),
                ('std1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='std1sc1', to='website.stdmodel')),
                ('std2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='std2sc1', to='website.stdmodel')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.subjectmodel')),
            ],
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='student1',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student1', to='website.stdmodel'),
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='student2',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student2', to='website.stdmodel'),
        ),
        migrations.CreateModel(
            name='GradeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A', models.IntegerField(null=True)),
                ('Bplus', models.IntegerField(null=True)),
                ('B', models.IntegerField(null=True)),
                ('Cplus', models.IntegerField(null=True)),
                ('C', models.IntegerField(null=True)),
                ('Dplus', models.IntegerField(null=True)),
                ('D', models.IntegerField(null=True)),
                ('F', models.IntegerField(null=True)),
                ('subject', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.subjectmodel')),
            ],
        ),
        migrations.CreateModel(
            name='FileProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('subscore', models.BooleanField(blank=True, default=False, null=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.projectmodel')),
                ('topic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.topicproject')),
            ],
        ),
        migrations.CreateModel(
            name='CoordinatorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.profmodel')),
            ],
        ),
    ]
