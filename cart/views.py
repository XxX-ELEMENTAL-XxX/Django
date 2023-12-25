from django.shortcuts import render
from .models import Shopping

def cart(request):
   products = Shopping.objects.order_by('-date')
   return render(request, 'cart/cart.html', {'products': products})
