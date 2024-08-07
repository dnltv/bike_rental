from celery import shared_task
from django.utils import timezone

from .models import Rental


@shared_task
def end_rental(rental_id):
    rental = Rental.objects.get(id=rental_id)
    rental.end_time = timezone.now()
    rental.save()
