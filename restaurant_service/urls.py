from django.urls import path
from .views import RestaurantView, MenuView

urlpatterns = [
    path('restaurant/<int:restaurant_id>/', RestaurantView.as_view(), name='restaurant_status'),
    path('restaurant/<int:restaurant_id>/menu/', MenuView.as_view(), name='add_menu_item'),
    path('menu/<int:menu_id>/', MenuView.as_view(), name='remove_menu_item'),
    path('restaurant/<int:restaurant_id>/menus/', MenuView.as_view(), name='get_all_menu_items'),
]