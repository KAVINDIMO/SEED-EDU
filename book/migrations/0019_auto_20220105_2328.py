# Generated by Django 3.1.3 on 2022-01-05 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0018_auto_20220105_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='bgrade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.booktypes'),
        ),
    ]
