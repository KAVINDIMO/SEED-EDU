# Generated by Django 3.1.3 on 2021-11-05 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0004_videos_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='description',
            field=models.CharField(blank=True, max_length=1500),
        ),
    ]