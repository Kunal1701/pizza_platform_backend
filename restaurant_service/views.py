from django.views import View
from django.http import JsonResponse
from .models import Restaurant, Menu
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist

@method_decorator(csrf_exempt, name='dispatch')
class RestaurantView(View):
    def post(self, request, restaurant_id):
        is_online = request.POST['is_online']
        restaurant = Restaurant.objects.get(id=restaurant_id)
        restaurant.is_online = is_online
        restaurant.save()
        return JsonResponse({'message': 'Restaurant status updated successfully'})

@method_decorator(csrf_exempt, name='dispatch')
class MenuView(View):
    def post(self, request, restaurant_id):
        pizza = request.POST['pizza']
        price = request.POST['price']
        restaurant = Restaurant.objects.get(id=restaurant_id)
        Menu.objects.create(restaurant=restaurant, pizza=pizza, price=price)
        return JsonResponse({'message': 'Menu item added successfully'})

    def delete(self, request, menu_id):
        menu_item = Menu.objects.get(id=menu_id)
        menu_item.delete()
        return JsonResponse({'message': 'Menu item removed successfully'})
    
    def get(self, request, restaurant_id):
        restaurant = Restaurant.objects.get(id=restaurant_id)
        menu_items = Menu.objects.filter(restaurant=restaurant)
        menu = []
        for item in menu_items:
            menu.append({'id': item.id, 'pizza': item.pizza, 'price': item.price})
        return JsonResponse({'menu': menu})