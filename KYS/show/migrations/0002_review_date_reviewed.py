# Generated by Django 2.1.3 on 2019-04-22 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date_reviewed',
            field=models.DateTimeField(auto_now=True),
        ),
    ]