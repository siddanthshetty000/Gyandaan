# Generated by Django 4.0.1 on 2022-01-26 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0020_service_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='schedule_id',
        ),
        migrations.AddField(
            model_name='appointment',
            name='service_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appointments.service'),
        ),
    ]