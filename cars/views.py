from django.shortcuts import render, redirect

from cars.models import Car
from cars import forms


def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search_string = request.GET.get('search')
    if search_string:
        cars = Car.objects.filter(model__contains=search_string)
    return render(request, 'cars.html', {'cars': cars})


def new_car_view(request):
    if request.method == 'POST':
        form = forms.CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cars_list')
    else:
        form = forms.CarForm()
    return render(request, 'new_car.html', {'form': form})

