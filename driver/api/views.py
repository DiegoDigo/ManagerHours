from rest_framework import generics
from driver.api.serializers import VeicleSerializer
from driver.models import Veicle


class Veicles(generics.ListAPIView):
    queryset = Veicle.objects.all()
    serializer_class = VeicleSerializer