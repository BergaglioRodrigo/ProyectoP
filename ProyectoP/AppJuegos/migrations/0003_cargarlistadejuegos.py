# Generated by Django 4.0.4 on 2022-05-27 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppJuegos', '0002_altajuego'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargarlistadejuegos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('desarrollador', models.CharField(max_length=40)),
                ('genero', models.CharField(max_length=40)),
                ('lanzamiento', models.DateField()),
                ('puntuacion', models.IntegerField()),
            ],
        ),
    ]