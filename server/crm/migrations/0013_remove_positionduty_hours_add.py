# Generated by Django 4.1.7 on 2023-02-28 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0012_positionduty_hours_duty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='positionduty',
            name='hours_add',
        ),
    ]