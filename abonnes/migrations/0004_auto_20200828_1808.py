# Generated by Django 3.0.8 on 2020-08-28 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abonnes', '0003_auto_20200828_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='langages',
            field=models.ManyToManyField(null=True, to='abonnes.Langage', verbose_name='Preciser vos Langages'),
        ),
    ]
