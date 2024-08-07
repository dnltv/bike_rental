from django.contrib.admin import ModelAdmin, register

from .models import CustomUser


@register(CustomUser)
class UserAdmin(ModelAdmin):
    search_fields = ('email', 'username')
    list_display = ('email', 'username')
    list_filter = ('email', 'username')
    empty_value_display = '-empty-'
