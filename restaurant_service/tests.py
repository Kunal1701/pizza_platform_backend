from django.test import TestCase, Client
from django.urls import reverse
from .models import Restaurant, Menu

class RestaurantViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.restaurant = Restaurant.objects.create(name='Test Restaurant', city='Test City', is_online=True)

    def test_restaurant_status(self):
        response = self.client.post(reverse('restaurant_status', args=[self.restaurant.id]), {'is_online': True})
        self.assertEqual(response.status_code, 200)
        self.restaurant.refresh_from_db()
        self.assertEqual(self.restaurant.is_online, True)

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.restaurant = Restaurant.objects.create(name='Test Restaurant', city='Test City', is_online=True)
        self.menu = Menu.objects.create(restaurant=self.restaurant, pizza='Test Pizza', price=10.00)

    def test_add_menu_item(self):
        response = self.client.post(reverse('add_menu_item', args=[self.restaurant.id]), {'pizza': 'New Pizza', 'price': 15.00})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Menu.objects.filter(restaurant=self.restaurant).count(), 2)

    def test_remove_menu_item(self):
        response = self.client.delete(reverse('remove_menu_item', args=[self.menu.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Menu.objects.filter(restaurant=self.restaurant).count(), 0)

    def test_get_all_menu_items(self):
        response = self.client.get(reverse('get_all_menu_items', args=[self.restaurant.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['menu']), 1)