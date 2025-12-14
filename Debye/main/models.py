from django.db import models


class Novosti(models.Model):
    title = models.CharField('Новости', max_length=100)
    intro = models.CharField('Анонс', max_length=1000)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
