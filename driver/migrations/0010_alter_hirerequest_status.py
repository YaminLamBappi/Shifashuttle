# Generated by Django 4.1.13 on 2024-05-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0009_remove_driver_ambulances_alter_ambulance_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hirerequest',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('completed', 'Completed')], default='pending', max_length=20),
        ),
    ]
