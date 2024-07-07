from django.shortcuts import render ,get_object_or_404
from .models import Product,Category
from cart.forms import CartAddProductForm

# Create your views here.


# here goes the views for the shop.abs

def product_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        
        products = products.filter(category=category)
        
        cart_product_form = CartAddProductForm()
        
        
    return render(
        request,
        'shop/product/list.html',
        {
            'category': category,
            'categories' : categories,
            'products' : products
        }
    )
    


# next view is product view for the 
def product_detail(request,id,slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    
    
    return render(
        request,
        'shop/product/detail.html',
        {
            'product': product
        }
    )