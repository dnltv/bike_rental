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

