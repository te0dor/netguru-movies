# Generated by Django 2.1.7 on 2019-02-22 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(help_text='Comment of movie', max_length=255)),
            ],
            options={
                'ordering': ['movie'],
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Movie title', max_length=255, unique=True)),
                ('year', models.IntegerField(blank=True, help_text='Movie year production', null=True)),
                ('description', models.TextField(blank=True, help_text='Movie plot', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(help_text='Related movie', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='movies.Movie'),
        ),
    ]
