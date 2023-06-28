from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='dashboard-index'),
    path('profesores/', views.profesores, name='dashboard-profesores'),
    path('material/', views.material, name='dashboard-material'),
    path('pedido/', views.pedido, name='dashboard-pedido'),
]