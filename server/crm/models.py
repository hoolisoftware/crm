import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy

User = get_user_model()


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

    dinner = models.BooleanField('Текущий обед', default=False)

    date = models.DateField('дата смены', default=timezone.now)
    position = models.CharField('должность', max_length=255)
    employee = models.ForeignKey(
        verbose_name='сотрудник', to=User, on_delete=models.CASCADE)
    paid = models.BooleanField('оплачено', default=False)

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
    def hours_int(self):
        return self.hours.seconds//3600

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
