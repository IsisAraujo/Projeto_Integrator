# Generated by Django 4.0.3 on 2022-03-04 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seriados', '0002_reviewepisodio_revisor_reviewepisodio_revisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodio',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
    ]
