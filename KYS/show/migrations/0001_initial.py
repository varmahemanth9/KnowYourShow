# Generated by Django 2.1.3 on 2019-04-13 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cast', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GENRE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genres', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(null=True)),
                ('Review', models.CharField(max_length=1000)),
                ('reviewer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleName', models.CharField(max_length=120)),
                ('releaseDate', models.DateField()),
                ('storyLine', models.CharField(max_length=2500)),
                ('budget', models.FloatField(null=True)),
                ('BoxOfficeCollection', models.FloatField(null=True)),
                ('titlePoster', models.ImageField(blank=True, upload_to='movie_posters')),
                ('titlePoster1', models.ImageField(blank=True, upload_to='movie_posters')),
                ('GENRE', models.ManyToManyField(to='show.GENRE')),
                ('cast', models.ManyToManyField(to='cast.cast')),
                ('director', models.ManyToManyField(to='cast.director')),
                ('language', models.ManyToManyField(to='show.language')),
                ('producer', models.ManyToManyField(to='cast.producer')),
                ('review', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='show.review')),
            ],
        ),
    ]
