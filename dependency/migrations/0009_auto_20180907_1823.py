# Generated by Django 2.0.3 on 2018-09-07 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dependency', '0008_auto_20180907_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='picture',
            field=models.URLField(blank=True, null=True),
        ),
    ]