from django.db import models
from django.contrib.auth.models import User

# app blog_app
# faq faq_app


# Category

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Названия')

    def __str__(self):
        return self.name

    class Meta:
        # отвечает за доп настройки таблицы
        verbose_name = 'Категория' # название таблицы в ед. числе
        verbose_name_plural = 'Категории' # название таблицы во мн. числе


class FAQ(models.Model):
    question = models.CharField(max_length=150, verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Вопрос-Ответ"
        verbose_name_plural = "Вопросы-Ответы"


class Slider(models.Model):
    title = models.CharField(max_length=75, verbose_name='Заголовок')
    subtitle = models.CharField(max_length=150, verbose_name='Подзаголовок')
    image = models.ImageField(upload_to='slider/', verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'

class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название', unique=True)
    short_description = models.TextField(verbose_name='Краткое описание')
    full_description = models.TextField(verbose_name='Полное описание')
    views = models.PositiveIntegerField(verbose_name='Просмотры', default=0)
    published_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    updated_add = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    preview = models.ImageField(verbose_name='Превью', upload_to='posts/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title

    def get_preview(self):
        if self.preview:
            return self.preview.url
        return 'https://1lag.com/wp-content/uploads/2021/12/simvolipubg2.png'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-published_at']

class PostGallery(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='gallery', verbose_name="Пост",
                             blank=True, null=True)
    photo = models.ImageField(upload_to='gallery/', blank=True, null=True)

    class Meta:
        verbose_name = 'Фото поста'
        verbose_name_plural = 'Фото поста'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments', verbose_name="Пост")
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='comments', verbose_name="Автор")
    text = models.TextField(verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return f"{self.post} - {self.author} - {self.created_at.date}"

    class Meta:
        verbose_name = "Коммент"
        verbose_name_plural = "Комменты"

class PostViews(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    session_id = models.TextField()

class Like(models.Model):
    user = models.ManyToManyField(User, related_name='likes')
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='likes')

class Dislike(models.Model):
    user = models.ManyToManyField(User, related_name='dislikes')
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='dislikes')