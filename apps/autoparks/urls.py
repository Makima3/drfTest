from django.urls import path

from .views import AutoParkListCreateAView, AutoParkRetrieveUpdateDestroyAView, AutoParkAddCarView

urlpatterns = [
    path('', AutoParkListCreateAView.as_view(), name='autopark_list_create'),
    path('/<int:pk>', AutoParkRetrieveUpdateDestroyAView.as_view(), name='autopark_retrieve_update_destroy'),
    path('/<int:pk>/add_car', AutoParkAddCarView.as_view(), name='autopark_add_car'),
]