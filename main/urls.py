from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='home'),
   path('cart', views.cart, name='cart'),
   path('setGurman', views.setGurman, name='setGurman'),
   path('setSensei', views.setSensei, name='setSensei'),
]
