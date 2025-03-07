from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('categories/<slug:slug>/', views.product_list_by_category, name='product_list_by_category'),
    path('categories/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('product/add/', views.product_add, name='product_add'),
]
