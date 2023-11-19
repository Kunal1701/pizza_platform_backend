from django.views import View
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import UserProfile, Order
from restaurant_service.models import Restaurant
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(View):
    """
    User Registration API

    POST fields:
    - username: String. Required.
    - password: String. Required.
    - city: String. Required.

    RESPONSES:
    - 200: User registered successfully.
    - 400: Username already taken or missing fields.
    """
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        city = request.POST.get('city')
        if not username or not password or not city:
            return HttpResponseBadRequest('Missing username, password, or city')
        if User.objects.filter(username=username).exists():
            return JsonResponse({'message': 'Username already taken'}, status=400)
        user = User.objects.create_user(username=username, password=password)
        UserProfile.objects.create(user=user, city=city)
        return JsonResponse({'message': 'User registered successfully'})

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    """
    User Login API

    POST fields:
    - username: String. Required.
    - password: String. Required.

    RESPONSES:
    - 200: Logged in successfully.
    - 400: Invalid credentials.
    """
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            return HttpResponseBadRequest('Missing username or password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Logged in successfully'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(View):
    """
    User Logout API

    POST fields: None

    RESPONSES:
    - 200: Logged out successfully.
    """
    @method_decorator(login_required)
    def post(self, request):
        logout(request)
        return JsonResponse({'message': 'Logged out successfully'})

@method_decorator(csrf_exempt, name='dispatch')
class RestaurantView(View):
    """
    Get Restaurants API

    GET fields: None

    RESPONSES:
    - 200: Returns a list of restaurants.
    """
    @method_decorator(login_required)
    def get(self, request):
        city = UserProfile.objects.get(user=request.user).city
        restaurants = Restaurant.objects.filter(city=city, is_online=True)
        return JsonResponse({'restaurants': list(restaurants.values())})

@method_decorator(csrf_exempt, name='dispatch')
class OrderView(View):
    """
    Order Pizza API

    POST fields:
    - restaurant: String. Required.
    - pizza: String. Required.

    RESPONSES:
    - 200: Order placed successfully.
    - 400: Missing restaurant or pizza.

    Get Orders API

    GET fields: None

    RESPONSES:
    - 200: Returns a list of orders.
    """
    @method_decorator(login_required)
    def post(self, request):
        user = request.user
        restaurant_name = request.POST.get('restaurant')
        pizza = request.POST.get('pizza')
        if not restaurant_name or not pizza:
            return HttpResponseBadRequest('Missing restaurant or pizza')
        try:
            restaurant = Restaurant.objects.get(name=restaurant_name, is_online=True)
        except Restaurant.DoesNotExist:
            return JsonResponse({'message': 'Restaurant does not exist or is not online'}, status=400)
        Order.objects.create(user=user, restaurant=restaurant.name, pizza=pizza)
        return JsonResponse({'message': 'Order placed successfully'})

    @method_decorator(login_required)
    def get(self, request):
        user = request.user
        orders = Order.objects.filter(user=user)
        return JsonResponse({'orders': list(orders.values())})