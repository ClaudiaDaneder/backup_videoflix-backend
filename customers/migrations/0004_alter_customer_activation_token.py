# Generated by Django 3.2 on 2024-06-28 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_alter_customer_activation_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='activation_token',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
