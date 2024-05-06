from django.urls import path

from .views import CarListView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarListView.as_view(), name='cars_list_create'), # ставимо пустті '' і прописуємо view на який має вести
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='cars_retrieve_update_destroy'), #  тут додаємо лище динамічну частину, яка додасться до основної урли cars
]