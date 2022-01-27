# Generated by Django 4.0.1 on 2022-01-21 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0006_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='mentor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appointments.mentor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='student_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appointments.student'),
        ),
    ]