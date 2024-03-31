from django.shortcuts import render, redirect
from django.views import View

from cars.models import Car
from cars import forms


class ListCarView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        cars = Car.objects.all().order_by('model')
        search_string = request.GET.get('search')
        if search_string:
            cars = Car.objects.filter(model__icontains=search_string)
        return render(request, 'cars.html', {'cars': cars})

class NewCarView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("login")
        form = forms.CarModelForm()
        return render(request, 'new_car.html', {'form': form})

    def post(self, request):
        form = forms.CarModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cars_list')
        else:
            return render(request, 'new_car.html', {'form': form})
