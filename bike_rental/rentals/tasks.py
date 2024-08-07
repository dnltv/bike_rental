from celery import shared_task
from django.conf import settings
from django.utils import timezone

from .models import Rental


@shared_task
def end_rental(rental_id):
    rental = Rental.objects.get(id=rental_id)
    rental.end_time = timezone.now()
    rental.save()
    duration = (rental.end_time - rental.start_time).total_seconds() / 3600
    cost = duration * settings.TEN
    return cost
