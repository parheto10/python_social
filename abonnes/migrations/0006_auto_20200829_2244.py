# Generated by Django 3.0.8 on 2020-08-29 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abonnes', '0005_auto_20200829_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='langages',
            field=models.ManyToManyField(help_text='Maintenez appuyé « Ctrl », ou « Commande (touche pomme) » sur un Mac, pour en sélectionner plusieurs.', to='abonnes.Langage', verbose_name='Preciser vos Langages'),
        ),
    ]
