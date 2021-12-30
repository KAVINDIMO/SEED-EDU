# Generated by Django 3.1.3 on 2021-10-08 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0013_assesedanswer_studentname'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddquizT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(default='quiz_name', max_length=200)),
                ('cgrade', models.IntegerField(default=10)),
            ],
        ),
        migrations.AlterField(
            model_name='addquestiont',
            name='testgrade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.addquizt'),
        ),
        migrations.DeleteModel(
            name='AddcourseT',
        ),
    ]
