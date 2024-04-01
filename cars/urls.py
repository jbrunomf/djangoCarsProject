from django.urls import path

from .views import CarDetailView

app_name = 'cars'
urlpatterns = [
    path('detail/<int:pk>/', CarDetailView.as_view(), name='car-detail')
]
