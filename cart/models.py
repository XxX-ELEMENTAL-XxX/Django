from django.db import models

class Shopping(models.Model):
   title = models.CharField('Назва', max_length=20)
   number = models.IntegerField('Кількість', max_length=3)
   date = models.DateTimeField('Час замовлення')

   def __str__(self):
      return self.title