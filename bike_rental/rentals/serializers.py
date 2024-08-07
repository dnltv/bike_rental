from rest_framework.serializers import ModelSerializer, ValidationError

from .models import Bike, Rental


class BikeSerializer(ModelSerializer):

    class Meta:
        model = Bike
        fields = ('name', 'is_available',)


class RentalSerializer(ModelSerializer):

    class Meta:
        model = Rental
        fields = ('user', 'bike', 'start_time', 'end_time',)

    def validate(self, data):
        if Rental.objects.filter(user=data['user'],
                                 end_time__isnull=True).exists():
            raise ValidationError(
                "User already has an active rental.")
        return data
