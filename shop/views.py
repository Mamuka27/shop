from django.shortcuts import render, get_object_or_404
from .models import Category

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'shop/category_list.html', {
        'categories': categories
    })

def product_list_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()  
    return render(request, 'shop/product_list.html', {
        'category': category,
        'products': products
    })
