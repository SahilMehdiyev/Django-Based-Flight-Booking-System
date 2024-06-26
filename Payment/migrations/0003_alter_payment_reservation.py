# Generated by Django 5.0.6 on 2024-05-29 10:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0002_remove_payment_amount_alter_payment_payment_method'),
        ('Reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='reservation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='Reservation.reservation'),
        ),
    ]
