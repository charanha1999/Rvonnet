from django.urls import path, include
from .views import ProductsList

urlpatterns = [
    path('', ProductsList.as_view(), name='products_list')
]