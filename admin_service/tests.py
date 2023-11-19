from django.test import TestCase, Client
from django.urls import reverse
from restaurant_service.models import Restaurant
from django.contrib.auth.models import User

class AdminViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin = User.objects.create_superuser(username='admin', password='adminpassword')
        self.client.login(username='admin', password='adminpassword')

    def test_add_restaurant(self):
        response = self.client.post(reverse('add_restaurant'), {'name': 'Test Restaurant', 'city': 'Test City'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Restaurant.objects.filter(name='Test Restaurant').exists())

    def test_remove_restaurant(self):
        restaurant = Restaurant.objects.create(name='Test Restaurant', city='Test City')
        response = self.client.delete(reverse('remove_restaurant', args=[restaurant.id]))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Restaurant.objects.filter(name='Test Restaurant').exists())