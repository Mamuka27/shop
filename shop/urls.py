from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('categories/<slug:slug>/', views.product_list_by_category, name='product_list_by_category'),
]
