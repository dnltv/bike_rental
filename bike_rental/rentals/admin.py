from django.contrib.admin import ModelAdmin, register, site

from .models import Bike, Rental

site.empty_value_display = '-empty-'


@register(Bike)
class BikeAdmin(ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'is_available')
    list_filter = ('name', 'is_available')


@register(Rental)
class RentalAdmin(ModelAdmin):
    search_fields = ('user', 'bike')
    list_display = ()
    list_filter = ()
