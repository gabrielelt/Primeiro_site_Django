# Generated by Django 5.0.1 on 2024-02-14 20:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0011_aluno_card_card_aluno'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno_card',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aluno_card', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='aluno_card',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aluno_card', to='cards.card'),
        ),
        migrations.AlterField(
            model_name='card',
            name='aluno',
            field=models.ManyToManyField(related_name='cards_respondidos', through='cards.Aluno_Card', to=settings.AUTH_USER_MODEL),
        ),
    ]