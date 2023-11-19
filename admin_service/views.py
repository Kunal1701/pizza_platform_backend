from django.views import View
from django.http import JsonResponse
from restaurant_service.models import Restaurant
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class AdminView(View):
    def post(self, request):
        name = request.POST['name']
        city = request.POST['city']
        Restaurant.objects.create(name=name, city=city)
        return JsonResponse({'message': 'Restaurant added successfully'})

    def delete(self, request, restaurant_id):
        restaurant = Restaurant.objects.get(id=restaurant_id)
        restaurant.delete()
        return JsonResponse({'message': 'Restaurant removed successfully'})