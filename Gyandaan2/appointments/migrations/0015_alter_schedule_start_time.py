# Generated by Django 4.0.1 on 2022-01-21 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0014_remove_service_estimated_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='start_time',
            field=models.DateTimeField(verbose_name='StartTime'),
        ),
    ]
