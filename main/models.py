from django.db import models

class SetOptions(models.Model):
   title = models.CharField('Назва', max_length=20)
   price = models.IntegerField('Ціна', max_length=5)
   grams = models.IntegerField('Грамів', max_length=6)
   composition = models.TextField('Склад')

   def __str__(self):
      return self.title
   