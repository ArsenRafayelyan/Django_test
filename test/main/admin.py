from django.contrib import admin
from .models import Category, SubCategory
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'category']
    list_display_links = ['id', 'name']
    search_fields = ['name']