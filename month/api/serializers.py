from rest_framework import serializers
from month.models import Month
from driver.api.serializers import VeicleSerializer

class MonthSerializer(serializers.ModelSerializer):
    
    veicle = VeicleSerializer()

    class Meta:
        model = Month
        fields = '__all__'