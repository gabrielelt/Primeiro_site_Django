# Generated by Django 5.0.1 on 2024-02-07 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_alter_card_resposta_correta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='resposta_correta',
            field=models.CharField(choices=[(models.CharField(max_length=100), 'PRIMEIRA ALTERNATIVA'), (models.CharField(max_length=100), models.CharField(max_length=100)), (models.CharField(max_length=100), models.CharField(max_length=100)), (models.CharField(max_length=100), models.CharField(max_length=100)), (models.CharField(max_length=100), models.CharField(max_length=100))], default='', max_length=100),
        ),
    ]
