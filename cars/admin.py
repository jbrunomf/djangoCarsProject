from django.contrib import admin

from cars.models import Car, Brand


# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'year', 'brand', 'model_year', 'value',)
    search_fields = ('model', 'year', 'brand',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
