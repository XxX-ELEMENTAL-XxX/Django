# Generated by Django 5.0 on 2023-12-25 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping',
            name='date',
            field=models.DateTimeField(verbose_name='Час замовлення'),
        ),
    ]