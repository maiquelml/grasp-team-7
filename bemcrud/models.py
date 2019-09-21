from django.db import models

class Person(models.Model):

  STATES = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
  )

  name = models.CharField(max_length=100, blank=False)
  cpf = models.CharField(max_length=11, blank=False, unique=True)
  rg = models.CharField(max_length=15, default=None, blank=True, null=True)
  dateOfBirth = models.DateField(default=None, blank=True, null=True)
  
  telephone = models.CharField(max_length=12, default=None, blank=True, null=True)
  cellphone = models.CharField(max_length=12, default=None, blank=True, null=True)
  email = models.CharField(max_length=100, default=None, blank=True, null=True)
  cep = models.CharField(max_length=8, default=None, blank=True, null=True)
  address = models.CharField(max_length=100, default=None, blank=True, null=True)
  addressNumber = models.IntegerField(default=None, blank=True, null=True)
  state = models.CharField(max_length=2, choices=STATES, default='SP', blank=True, null=True)

  def __str__(self):
    return self.name

class Request(models.Model):

  cpf = models.CharField(max_length=11, blank=False)
  value = models.DecimalField(max_digits=10, blank=False, decimal_places=2)
  installments = models.IntegerField(blank=False, default=1)
  date = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.cpf