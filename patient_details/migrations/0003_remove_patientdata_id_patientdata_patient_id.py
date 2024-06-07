# Generated by Django 4.2.13 on 2024-06-07 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_details', '0002_patientdata_symptoms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientdata',
            name='id',
        ),
        migrations.AddField(
            model_name='patientdata',
            name='patient_id',
            field=models.CharField(default='NULL', max_length=10, primary_key=True, serialize=False),
        ),
    ]