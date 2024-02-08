# Generated by Django 5.0.1 on 2024-02-02 11:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='resposta',
            new_name='alternativa_dois',
        ),
        migrations.AddField(
            model_name='card',
            name='alternativa_quatro',
            field=models.CharField(default=datetime.datetime(2024, 2, 2, 11, 26, 24, 764671, tzinfo=datetime.timezone.utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='alternativa_tres',
            field=models.CharField(default=datetime.datetime(2024, 2, 2, 11, 27, 21, 910674, tzinfo=datetime.timezone.utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='alternativa_um',
            field=models.CharField(default=datetime.datetime(2024, 2, 2, 11, 27, 32, 662741, tzinfo=datetime.timezone.utc), max_length=100),
            preserve_default=False,
        ),
    ]
