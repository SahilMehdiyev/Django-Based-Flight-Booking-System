# Generated by Django 5.0.6 on 2024-05-29 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='amount',
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'), ('paypal', 'PayPal'), ('bank_transfer', 'Bank Transfer')], max_length=20),
        ),
    ]
