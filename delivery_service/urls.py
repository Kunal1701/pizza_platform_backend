from django.urls import path
from .views import DeliveryView

urlpatterns = [
    path('delivery/<int:order_id>/', DeliveryView.as_view(), name='delivery'),
]