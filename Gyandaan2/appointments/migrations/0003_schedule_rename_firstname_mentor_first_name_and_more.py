# Generated by Django 4.0.1 on 2022-01-21 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_remove_mentor_name_remove_student_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.RenameField(
            model_name='mentor',
            old_name='FirstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='mentor',
            old_name='LastName',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='FirstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='LastName',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='student',
            name='schedule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appointments.schedule'),
        ),
    ]