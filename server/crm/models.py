import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy

User = get_user_model()


class Project(models.Model):
    name = models.CharField('название', max_length=55)
    description = models.TextField('описание', blank=True, null=True)
    employees = models.ManyToManyField(to=User, verbose_name='сотрудники', related_name='projects_employee', blank=True) # noqa ignore
    owner = models.ForeignKey(User, verbose_name='владелец', on_delete=models.CASCADE, related_name='projects_owner') # noqa ignore


class Duty(models.Model):
    address = models.CharField('адрес', max_length=255)
    km = models.IntegerField('км за МКАД', default=0)
    hours_duty = models.IntegerField('длительность смены (ч)', default=9)
    hours_since_last = models.FloatField('разрыв между сменами', default=12)
    price = models.IntegerField('цена часа смены')
    price_add = models.IntegerField('цена часа переработки')
    price_km = models.IntegerField('цена км за МКАД')
    start = models.TimeField('начало смены', default=timezone.now)
    end = models.TimeField('конец смены', default=timezone.now)
    days = models.IntegerField('кол-во суток в смене', default=0)

    hours_dinner_fluent = models.IntegerField('Текущий обед (ч)', default=2)
    hours_dinner_late = models.IntegerField('Поздний обед (ч)', default=0)

    date = models.DateField('дата смены', default=timezone.now)
    position = models.CharField('должность', max_length=255)
    employee = models.ForeignKey(
        verbose_name='сотрудник', to=User, on_delete=models.CASCADE)
    paid = models.BooleanField('оплачено', default=False)

    project = models.ForeignKey(Project, verbose_name='Проект', on_delete=models.CASCADE, null=True, blank=True) # noqa ignore

    @property
    def start_datetime(self):
        return f'{self.date} {self.start.strftime("%H:%M")}'

    @property
    def end_datetime(self):
        return f'{self.date + datetime.timedelta(days=self.days)} {self.end.strftime("%H:%M")}' # noqa ignore

    @property
    def hours(self):
        return datetime.datetime.strptime(self.end.strftime('%H:%M'), '%H:%M') - datetime.datetime.strptime(self.start.strftime('%H:%M'), '%H:%M') # noqa ignore

    @property
    def hours_add(self):
        return max(self.hours_int - self.hours_duty, 0)

    @property
    def hours_add_sum(self):
        return self.hours_add + self.hours_dinner_fluent + self.hours_dinner_late + self.hours_insomnia # noqa ignore

    @property
    def hours_int(self):
        return self.hours.seconds//3600

    @property
    def hours_insomnia(self):
        return max(12 - self.hours_since_last, 0)

    @property
    def price_sum(self):
        return self.hours_duty * self.price + self.hours_add_sum * self.price_add + self.price_km * self.km # noqa ignore

    class Meta:
        abstract = True

    def get_absolute_url(self):
        return reverse_lazy('crm:account-duty-detail', args=[self.id])


class PositionDuty(Duty):
    class Meta:
        verbose_name = 'смена'
        verbose_name_plural = 'смены'

    def __str__(self):
        return self.employee.get_full_name()
