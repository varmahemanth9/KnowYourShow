# Generated by Django 2.1.7 on 2019-04-06 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0003_auto_20190406_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='show.review'),
        ),
    ]
