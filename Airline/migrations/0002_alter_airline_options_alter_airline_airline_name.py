# Generated by Django 5.0.6 on 2024-05-31 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Airline', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='airline',
            options={'verbose_name': 'Airline', 'verbose_name_plural': 'Airlines'},
        ),
        migrations.AlterField(
            model_name='airline',
            name='airline_name',
            field=models.TextField(max_length=100),
        ),
    ]