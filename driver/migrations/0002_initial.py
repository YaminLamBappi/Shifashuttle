# Generated by Django 4.1.13 on 2024-05-20 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='callhistory',
            name='call',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver.call'),
        ),
        migrations.AddField(
            model_name='call',
            name='assigned_ambulance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='driver.ambulance'),
        ),
        migrations.AddField(
            model_name='call',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
