from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile, Order

class UserViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user_profile = UserProfile.objects.create(user=self.user, city='Test City')

    def test_register(self):
        response = self.client.post(reverse('register'), {'username': 'newuser', 'password': 'newpassword', 'city': 'New City'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 200)

class RestaurantViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user_profile = UserProfile.objects.create(user=self.user, city='Test City')
        self.client.login(username='testuser', password='testpassword')

    def test_get_restaurants(self):
        response = self.client.get(reverse('restaurants'))
        self.assertEqual(response.status_code, 200)

class OrderViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user_profile = UserProfile.objects.create(user=self.user, city='Test City')
        self.order = Order.objects.create(user=self.user, restaurant='Test Restaurant', pizza='Test Pizza')
        self.client.login(username='testuser', password='testpassword')

    def test_order_pizza(self):
        response = self.client.post(reverse('order'), {'restaurant': 'Test Restaurant', 'pizza': 'New Pizza'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Order.objects.filter(user=self.user).count(), 1)

    def test_get_orders(self):
        response = self.client.get(reverse('orders'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['orders']), 1)