# Generated by Django 2.2.5 on 2019-09-21 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bemcrud', '0003_auto_20190919_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='rg',
            field=models.CharField(blank=True, default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='person',
            name='telephone',
            field=models.CharField(default='', max_length=12),
        ),
    ]