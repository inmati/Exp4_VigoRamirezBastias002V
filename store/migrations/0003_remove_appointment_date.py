# Generated by Django 4.0.5 on 2022-06-22 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_appointment_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='date',
        ),
    ]
