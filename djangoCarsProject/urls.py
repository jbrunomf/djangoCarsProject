from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from cars.views import cars_view, new_car_view
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', cars_view, name='cars_list'),
    path('new_car/', new_car_view, name='new_car'),
    path('register/', accounts_views.register_view, name='register'),
    path('login/', accounts_views.login_view, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
