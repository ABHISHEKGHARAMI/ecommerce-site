from django.contrib import admin
from .models import Category,Product

# Register your models here.

# first register the Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
    
    
    
# second register the Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price',
                    'available','created','updated']
    list_filter = ['available','created','updated']
    list_editable = ['price','available']
    prepopulated_fields = {'slug' : ('name',)}
