# Generated by Django 4.0.1 on 2022-01-26 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0023_remove_appointment_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='meeting_link',
            field=models.TextField(null=True),
        ),
    ]