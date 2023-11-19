from django.test import TestCase, Client
from django.urls import reverse
from user_service.models import Order
from .models import Delivery
from django.contrib.auth.models import User

class DeliveryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user(username='testuser', password='testpassword')
        self.order = Order.objects.create(user=self.test_user, restaurant='Test Restaurant', pizza='Test Pizza', status='Pending')
        self.delivery = Delivery.objects.create(order=self.order, status='Pending')

    def test_update_delivery_status(self):
        response = self.client.post(reverse('delivery', args=[self.order.id]), {'status': 'Delivered'})
        self.assertEqual(response.status_code, 200)
        self.delivery.refresh_from_db()
        self.assertEqual(self.delivery.status, 'Pending')