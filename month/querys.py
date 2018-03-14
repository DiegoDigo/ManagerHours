from __future__ import unicode_literals
from django.db.models.query import QuerySet


class MonthQuerySet(QuerySet):
    
    def get_month(self, month: int, year: int) -> QuerySet:
        return self.filter(day__month=month,
                           day__year=year)
