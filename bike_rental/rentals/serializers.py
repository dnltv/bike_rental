from rest_framework.serializers import ModelSerializer
from .models import Bike, Rental


class BikeSerializer(ModelSerializer):
    class Meta:
        model = Bike
        fields = ('name', 'is_available',)


class RentalSerializer(ModelSerializer):
    class Meta:
        model = Rental
        fields = ('bike', 'start_time', 'end_time',)
