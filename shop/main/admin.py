from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    # list_display те параметры которые есть в моделы которые мы будем отобрадать в админке 
    prepopulated_fields = {'slug' : ('name',)}
    # prepopulated_fields - поля которыеп будут заполнены автоматически

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','price','available','created','updated' ]
    list_filter = ['available', 'created','updated','category']
    # то по каким параметрам можно будет фильтровать
    list_editable = ['price', 'available']
    # параметры которые можно изменять
    prepopulated_fields = {'slug' : ('name',)}