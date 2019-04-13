# Generated by Django 2.1.3 on 2019-04-11 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cast', '0011_director_producer'),
        ('show', '0010_auto_20190410_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='director',
        ),
        migrations.AddField(
            model_name='show',
            name='director',
            field=models.ManyToManyField(to='cast.director'),
        ),
        migrations.RemoveField(
            model_name='show',
            name='producer',
        ),
        migrations.AddField(
            model_name='show',
            name='producer',
            field=models.ManyToManyField(to='cast.producer'),
        ),
    ]