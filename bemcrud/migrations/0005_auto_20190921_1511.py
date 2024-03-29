# Generated by Django 2.2.5 on 2019-09-21 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bemcrud', '0004_auto_20190921_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='addressNumber',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='person',
            name='cellPhone',
            field=models.CharField(blank=True, default=None, max_length=12),
        ),
        migrations.AlterField(
            model_name='person',
            name='cep',
            field=models.CharField(blank=True, default=None, max_length=8),
        ),
        migrations.AlterField(
            model_name='person',
            name='dateOfBirth',
            field=models.DateField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='state',
            field=models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='SP', max_length=2),
        ),
        migrations.AlterField(
            model_name='person',
            name='telephone',
            field=models.CharField(blank=True, default=None, max_length=12),
        ),
    ]
