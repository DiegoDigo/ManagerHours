from rest_framework import serializers
from driver.models import Veicle


class VeicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veicle
        fields = '__all__'