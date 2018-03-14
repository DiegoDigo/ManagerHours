from django.contrib import admin
from month.models import Month


class AdminMonth(admin.ModelAdmin):
    list_display = ['day', 'hours_entry', 'hours_exit', 'total_hours']


admin.site.register(Month, AdminMonth)