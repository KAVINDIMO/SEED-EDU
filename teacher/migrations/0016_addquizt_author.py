# Generated by Django 3.1.3 on 2021-10-08 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0015_auto_20211008_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='addquizt',
            name='author',
            field=models.CharField(default='teacher_name', max_length=200),
        ),
    ]