# Generated by Django 2.2.7 on 2020-10-28 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie_cast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actors', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Overview_tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('overview', models.CharField(max_length=255)),
                ('poster_url', models.URLField()),
                ('release_date', models.DateTimeField()),
                ('adult', models.BooleanField()),
                ('runningtime', models.TimeField()),
                ('vote_average', models.FloatField(max_length=11)),
                ('rating', models.FloatField(max_length=11)),
                ('genres', models.ManyToManyField(related_name='movie_genre', to='movies.Genre')),
                ('movie_casts', models.ManyToManyField(related_name='movie_cast', to='movies.Movie_cast')),
                ('overview_tags', models.ManyToManyField(related_name='overview_tag', to='movies.Overview_tag')),
            ],
        ),
    ]