from django.urls import path

from .views import cars_view

app_name = 'cars'
urlpatterns = [
    path('', cars_view)
]
