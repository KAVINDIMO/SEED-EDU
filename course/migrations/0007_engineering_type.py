# Generated by Django 3.1.2 on 2021-11-07 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20211107_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='engineering',
            name='type',
            field=models.CharField(default='BTECH', max_length=10),
        ),
    ]
