# Generated by Django 4.2.4 on 2023-08-07 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_prices_options_remove_prices_aluminum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prices',
            name='metal',
            field=models.CharField(max_length=20, verbose_name='Металл'),
        ),
        migrations.AlterField(
            model_name='prices',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]
