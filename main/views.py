from django.shortcuts import render
from .models import SetOptions

def index(request):
   set = SetOptions.objects.all()
   return render(request, 'main/index.html', {'set': set})

def cart(request):
   return render(request, 'main/cart.html')

def setGurman(request):
   set = SetOptions.objects.all()
   return render(request, 'main/set-gurman.html', {'set': set})


def setSensei(request):
   set = SetOptions.objects.all()
   return render(request, 'main/set-sensei.html', {'set': set})
