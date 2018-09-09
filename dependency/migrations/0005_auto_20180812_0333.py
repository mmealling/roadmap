# Generated by Django 2.0.3 on 2018-08-12 03:33

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dependency', '0004_auto_20180308_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('author2', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('subgenre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='bar')),
                ('year', models.SmallIntegerField()),
                ('tags', models.TextField()),
                ('editions', models.TextField()),
                ('goodreads', models.TextField()),
                ('isbn', models.CharField(max_length=100)),
                ('asin', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('rating', models.SmallIntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '**** '), (5, '*****')], null=True)),
                ('description', models.TextField()),
                ('director', models.CharField(max_length=200)),
                ('links', models.URLField(max_length=1000)),
                ('picture', models.ImageField(upload_to='bar')),
                ('year', models.SmallIntegerField()),
                ('production_company', models.CharField(max_length=200)),
                ('motto', models.TextField()),
                ('genre', models.CharField(max_length=200)),
                ('cast', models.TextField()),
                ('video', models.URLField(max_length=1000)),
                ('violence', models.SmallIntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '**** '), (5, '*****')], null=True)),
                ('nudity', models.SmallIntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '**** '), (5, '*****')], null=True)),
                ('horror', models.SmallIntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '**** '), (5, '*****')], null=True)),
                ('mpaa_rating', models.CharField(choices=[('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('N/A', 'N/A')], max_length=5, null=True)),
                ('trivia', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='tasks',
            name='document',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='enddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='startdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]