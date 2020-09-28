# Generated by Django 3.0.8 on 2020-09-24 19:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleToGroup',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('group_id', models.CharField(max_length=30, verbose_name='分组ID')),
                ('article_id', models.CharField(max_length=30, verbose_name='文章ID')),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='tag名称')),
                ('create_date_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['name'],
                'default_permissions': (),
            },
        ),
    ]