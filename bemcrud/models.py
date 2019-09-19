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
  rg = models.CharField(max_length=15, default=None)
  dateOfBirth = models.DateField(default=None)
  
  telephone = models.CharField(max_length=12, default=None)
  cellPhone = models.CharField(max_length=12, default=None)
  email = models.CharField(max_length=100, default=None)
  cep = models.CharField(max_length=8, default=None)
  address = models.CharField(max_length=100, default=None)
  addressNumber = models.IntegerField(default=None)
  state = models.CharField(max_length=2, choices=STATES, default='SP')

  def __str__(self):
    return self.name