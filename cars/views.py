from django.views.generic import ListView, CreateView

from cars.models import Car
from cars import forms


class ListCarView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search)
        return cars


class NewCarView(CreateView):
    model = Car
    form_class = forms.CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'