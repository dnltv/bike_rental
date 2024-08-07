from django.conf import settings
from django.db import models


class Bike(models.Model):
    """
    Модель для представления велосипеда.
    """

    name = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Велосипед'
        verbose_name_plural = 'Велосипеды'

    def __str__(self):
        return self.name


class Rental(models.Model):
    """
    Модель для представления аренды велосипеда.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
