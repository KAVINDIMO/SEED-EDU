# Generated by Django 3.1.3 on 2021-10-07 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20211005_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='mockanswer',
            name='correctedanswersheet',
            field=models.FileField(default='static/images/default.pdf', upload_to='images'),
        ),
    ]
