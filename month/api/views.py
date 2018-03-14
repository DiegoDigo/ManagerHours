from rest_framework import generics
from month.api.serializers import MonthSerializer
from month.models import Month


class Months(generics.ListAPIView):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer