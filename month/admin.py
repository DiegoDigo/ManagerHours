from django.contrib import admin
from month.models import Month


class AdminMounth(admin.ModelAdmin):
    list_display = ['day', 'hours_entry', 'hours_exit', 'total_hours']


admin.site.register(Month, AdminMounth)