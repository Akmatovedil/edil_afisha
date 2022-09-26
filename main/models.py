from django.db import models

# Create your models here.


class Film (models.Model):
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
    name = models.CharField(max_length=100, verbose_name='Название')
    producer = models.TextField(null=True, verbose_name='Режиссер')
    rating = models.FloatField(default=0, verbose_name='Рейтинг')
    duration = models.IntegerField(null=True, verbose_name='Длительность')


    def __str__(self):
        return self.name


class Review (models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, null=True)
    text = models.TextField()

    def __str__(self):
        return self.text
