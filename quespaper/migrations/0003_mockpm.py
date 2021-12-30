# Generated by Django 3.1.3 on 2021-09-23 15:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quespaper', '0002_auto_20210818_0040'),
    ]

    operations = [
        migrations.CreateModel(
            name='MockPM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mockpapername', models.CharField(max_length=200)),
                ('paperdescription', models.CharField(default='The description', max_length=100)),
                ('forgrade', models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(10)])),
                ('mockpaper', models.FileField(upload_to='images')),
            ],
        ),
    ]
