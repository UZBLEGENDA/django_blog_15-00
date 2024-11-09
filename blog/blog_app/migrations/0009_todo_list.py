# Generated by Django 4.1.3 on 2024-11-02 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_alter_post_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, unique=True, verbose_name='Название')),
                ('short_description', models.TextField(verbose_name='Краткое описание')),
                ('full_description', models.TextField(verbose_name='Полное описание')),
                ('published_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('updated_add', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Задачи',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
