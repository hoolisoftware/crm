# Generated by Django 4.1.7 on 2023-02-26 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_alter_positionduty_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='positionduty',
            name='address',
            field=models.CharField(default='', max_length=255, verbose_name='адрес'),
            preserve_default=False,
        ),
    ]
