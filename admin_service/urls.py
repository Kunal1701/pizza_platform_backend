from django.urls import path
from .views import AdminView

urlpatterns = [
    path('admin/restaurant/', AdminView.as_view(), name='add_restaurant'),
    path('admin/restaurant/<int:restaurant_id>/', AdminView.as_view(), name='remove_restaurant'),
]