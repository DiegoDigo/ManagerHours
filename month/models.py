from django.db import models
from driver.models import Veicle
from month.querys import MonthQuerySet
from utility import utility

class Month(models.Model):
    day = models.DateField(auto_now=False, auto_now_add=False, unique=True)
    hours_entry = models.TimeField(auto_now=False, auto_now_add=False)
    hours_exit = models.TimeField(auto_now=False, auto_now_add=False)
    period_hour_entry = models.TimeField(auto_now=False, auto_now_add=False)
    period_hour_exit = models.TimeField(auto_now=False, auto_now_add=False)
    total_hours = models.CharField(max_length=25, null=True, blank=True)
    veicle = models.ForeignKey(Veicle, on_delete='cascate')
    objects = MonthQuerySet().as_manager()

    def __str__(self):
        return str(self.day)

    def save(self, *args, **kwargs):    
        self.total_hours = utility.bank_of_hours(self.period_hour_entry, self.hours_entry,
                                                 self.period_hour_exit, self.hours_exit)
        super(Month, self).save(*args, **kwargs)
        
    
    class Meta:
        verbose_name_plural = 'Months'
        verbose_name = 'Month'