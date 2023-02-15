# Generated by Django 4.1.6 on 2023-02-15 03:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
                ('daily_salary', models.IntegerField(verbose_name='цена смены')),
                ('daily_salary_additional', models.IntegerField(verbose_name='цена часа переработки')),
                ('daily_hours', models.IntegerField(verbose_name='кол-во часов в смене')),
                ('daily_hours_spread', models.IntegerField(verbose_name='разрыв между сменами (часы)')),
                ('employee', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='сотрудники')),
            ],
            options={
                'verbose_name': 'должность',
                'verbose_name_plural': 'должности',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('created', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='владелец')),
            ],
            options={
                'verbose_name': 'проект',
                'verbose_name_plural': 'проекты',
            },
        ),
        migrations.CreateModel(
            name='PositionMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='дата отметки')),
                ('paid', models.BooleanField(verbose_name='оплачено')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='сотрудник')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.position', verbose_name='позиция')),
            ],
            options={
                'verbose_name': 'метка',
                'verbose_name_plural': 'метки',
            },
        ),
        migrations.CreateModel(
            name='PositionAdditionalMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='дата отметки')),
                ('paid', models.BooleanField(verbose_name='оплачено')),
                ('hours', models.IntegerField(verbose_name='кол-во часов')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='сотрудник')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.position', verbose_name='позиция')),
            ],
            options={
                'verbose_name': 'метка (сверхурочная)',
                'verbose_name_plural': 'метки (сверхурочные)',
            },
        ),
        migrations.AddField(
            model_name='position',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.project', verbose_name='проект'),
        ),
    ]
