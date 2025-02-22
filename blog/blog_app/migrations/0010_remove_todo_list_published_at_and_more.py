# Generated by Django 4.1.3 on 2024-11-06 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_todo_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo_list',
            name='published_at',
        ),
        migrations.RemoveField(
            model_name='todo_list',
            name='updated_add',
        ),
        migrations.AddField(
            model_name='todo_list',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время заканчивание'),
        ),
        migrations.AddField(
            model_name='todo_list',
            name='time_completed',
            field=models.DateTimeField(auto_now=True, verbose_name='Время выполнения'),
        ),
        migrations.AlterField(
            model_name='todo_list',
            name='full_description',
            field=models.TextField(verbose_name='Полное описание задачи'),
        ),
        migrations.AlterField(
            model_name='todo_list',
            name='short_description',
            field=models.TextField(verbose_name='Краткое описание задачи'),
        ),
    ]
