from django.db import models
from django.urls import reverse

class BaseWords(models.Model):
    base_word = models.CharField(max_length=4, verbose_name='слово')

    def __str__(self):
        return self.base_word

    class Meta:
        verbose_name = 'Cлово из базы данных'
        verbose_name_plural = 'Слова из базы данных'
        ordering = ["base_word"]
