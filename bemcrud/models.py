from django.db import models

class Person(models.Model):

  name = models.CharField(max_length=100)
  cpf = models.CharField(max_length=11)
  phone = models.CharField(max_length=12, default='')
  address = models.CharField(max_length=100, default='')
  addressNumber = models.IntegerField(default=None)

  def __str__(self):
    return self.name