# Generated by Django 4.0.1 on 2022-01-21 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0011_appointment_cancellation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateField(verbose_name='StartTime')),
                ('end_time', models.DateTimeField(verbose_name='EndTime')),
                ('mentor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appointments.mentor')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=128, null=True)),
                ('estimated_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceBooked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProvided',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='subject_id',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.AddField(
            model_name='serviceprovided',
            name='appointment_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appointments.appointment'),
        ),
        migrations.AddField(
            model_name='serviceprovided',
            name='service_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appointments.service'),
        ),
        migrations.AddField(
            model_name='servicebooked',
            name='appointment_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appointments.appointment'),
        ),
        migrations.AddField(
            model_name='servicebooked',
            name='service_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appointments.service'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='schedule_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appointments.schedule'),
        ),
    ]
