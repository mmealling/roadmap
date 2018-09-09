# Generated by Django 2.0.3 on 2018-09-07 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dependency', '0007_auto_20180812_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
        migrations.AddField(
            model_name='movie',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='elementID',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
