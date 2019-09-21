# Generated by Django 2.2.5 on 2019-09-21 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bemcrud', '0008_auto_20190921_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
