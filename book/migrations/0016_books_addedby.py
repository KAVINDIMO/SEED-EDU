# Generated by Django 3.1.3 on 2022-01-02 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0015_books_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='addedby',
            field=models.CharField(default='Admin', max_length=1000),
        ),
    ]