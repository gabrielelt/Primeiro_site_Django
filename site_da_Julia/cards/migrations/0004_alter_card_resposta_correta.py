# Generated by Django 5.0.1 on 2024-02-07 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_card_alternativa_cinco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='resposta_correta',
            field=models.CharField(choices=[(models.CharField(max_length=100), models.CharField(max_length=100)), (models.CharField(max_length=100), models.CharField(max_length=100)), (models.CharField(max_length=100), models.CharField(max_length=100)), (models.CharField(max_length=100), models.CharField(max_length=100)), (models.CharField(max_length=100), models.CharField(max_length=100))], default='', max_length=100),
        ),
    ]
