from django.shortcuts import render

from cars.models import Car


def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search_string = request.GET.get('search')
    if search_string:
        cars = Car.objects.filter(model__contains=search_string)
    return render(request, 'cars.html', {'cars': cars})
