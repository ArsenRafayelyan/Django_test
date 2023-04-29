from django.shortcuts import render
from .models import Category, SubCategory
# Create your views here.


def index(request):
    category_list = Category.objects.all()
    return render(request, 'main/index.html', context={
        'category_list':category_list
    })


def index_detail(request, slug):
    category_list = Category.objects.all()
    item = SubCategory.objects.get(slug=slug)
    return render(request, 'main/index_detail.html', context={
        'item':item,
        'category_list':category_list
    })
