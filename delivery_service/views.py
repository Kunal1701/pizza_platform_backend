from django.views import View
from django.http import JsonResponse
from .models import Delivery
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from user_service.models import Order

@method_decorator(csrf_exempt, name='dispatch')
class DeliveryView(View):
    def post(self, request, order_id):
        status = request.POST.get('status')
        try:
            order = Order.objects.get(id=order_id)
            order.status = status
            order.save()
            return JsonResponse({'message': 'Delivery status updated successfully'})
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Delivery with given order_id does not exist'}, status=400)