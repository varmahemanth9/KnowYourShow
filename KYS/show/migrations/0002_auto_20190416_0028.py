# Generated by Django 2.1.3 on 2019-04-15 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='review',
        ),
        migrations.AddField(
            model_name='review',
            name='show',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='show.Show'),
        ),
    ]
