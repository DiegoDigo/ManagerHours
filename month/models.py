from django.db import models
from driver.models import Veicle
from month.querys import MonthQuerySet

class Month(models.Model):
    day = models.DateField(auto_now=False, auto_now_add=False, unique=True)
    hours_entry = models.TimeField(auto_now=False, auto_now_add=False)
    hours_exit = models.TimeField(auto_now=False, auto_now_add=False)
    total_hours = models.CharField(max_length=8)
    veicle = models.ForeignKey(Veicle, on_delete='cascate')
    objects = MonthQuerySet().as_manager()

    def __str__(self):
        return str(self.day)

    class Meta:
        verbose_name_plural = 'Months'
        verbose_name = 'Month'
