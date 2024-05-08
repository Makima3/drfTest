from django.urls import path

from .views import AutoParkListCreateView, AutoParkAddCarsView

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='autoparks_list_create'),
    path('/<int:pk>/add_car', AutoParkAddCarsView.as_view(), name='autoparks_add_car')
]