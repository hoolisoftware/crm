from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Project(models.Model):
    name = models.CharField('название', max_length=255)
    description = models.TextField('описание')
    created = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(verbose_name='владелец',
                              to=User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'

    def __str__(self):
        return self.name


class Position(models.Model):
    project = models.ForeignKey(
        verbose_name='проект', to=Project, on_delete=models.CASCADE)
    employee = models.ManyToManyField(verbose_name='сотрудники', to=User)
    name = models.CharField('название', max_length=255)
    daily_salary = models.IntegerField('цена смены')
    daily_salary_additional = models.IntegerField('цена часа переработки')
    daily_hours = models.IntegerField('кол-во часов в смене')
    daily_hours_spread = models.IntegerField('разрыв между сменами (часы)')

    class Meta:
        verbose_name = 'должность'
        verbose_name_plural = 'должности'

    def __str__(self):
        return self.name


class Mark(models.Model):
    date = models.DateField('дата отметки')
    position = models.ForeignKey(
        verbose_name='позиция', to=Position, on_delete=models.CASCADE)
    employee = models.ForeignKey(
        verbose_name='сотрудник', to=User, on_delete=models.CASCADE)
    paid = models.BooleanField('оплачено')

    class Meta:
        abstract = True


class PositionMark(Mark):
    class Meta:
        verbose_name = 'метка'
        verbose_name_plural = 'метки'

    def __str__(self):
        return self.employee.get_full_name()


class PositionAdditionalMark(Mark):
    hours = models.IntegerField('кол-во часов')

    class Meta:
        verbose_name = 'метка (сверхурочная)'
        verbose_name_plural = 'метки (сверхурочные)'

    def __str__(self):
        return self.employee.get_full_name()
