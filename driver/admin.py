from django.contrib import admin
from .models import Veicle


class AdminVeicle(admin.ModelAdmin):
    list_display = ['name_line', 'numer_line', 'numer_car' ]


admin.site.register(Veicle, AdminVeicle)