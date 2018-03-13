from django.db import models

class Mounth(models.Model):
    day = models.DateField(auto_now=False, auto_now_add=False, unique=True)
    hours_entry = models.TimeField(auto_now=False, auto_now_add=False)
    
