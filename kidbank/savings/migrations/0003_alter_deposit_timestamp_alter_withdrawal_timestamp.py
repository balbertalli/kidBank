# Generated by Django 4.1.5 on 2023-01-21 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0002_deposit_withdrawal_delete_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]