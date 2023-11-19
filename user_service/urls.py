from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('restaurants/', RestaurantView.as_view(), name='restaurants'),
    path('order/', OrderView.as_view(), name='order'),
    path('orders/', OrderView.as_view(), name='orders'),
]