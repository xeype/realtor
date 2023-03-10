# Generated by Django 4.1.7 on 2023-02-28 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtor_app', '0010_alter_services_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_rooms', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realtor_app.employees')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realtor_app.prices')),
            ],
        ),
        migrations.CreateModel(
            name='Agreements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realtor_app.apartments')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realtor_app.customers')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realtor_app.employees')),
            ],
        ),
    ]
