# Generated by Django 2.2.5 on 2019-09-21 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bemcrud', '0010_auto_20190921_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='installments',
            field=models.IntegerField(default=1),
        ),
    ]
