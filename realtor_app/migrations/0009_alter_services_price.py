# Generated by Django 4.1.7 on 2023-02-27 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtor_app', '0008_rename_amount_prices_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='price',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='realtor_app.prices'),
        ),
    ]
