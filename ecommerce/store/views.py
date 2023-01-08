from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.

def store(request):
    #get all products and put them into context object
    all_products = Product.objects.all()
    context = {'all_products': all_products}

    #because we have our template folder nested under store we need to add that path here also send through the context
    return render(request, 'store/store.html', context)


def categories(request):
    #get all categories from the model
    all_categories = Category.objects.all()
    
    #need to get this data to every page so that it can be used for the navbar
    #see settings.py to see where it is added
    return {'all_categories': all_categories}

#slug comes from url <slug:slug>
def product_info(request, slug):
    #find product that has the same slug as url slug or return not found
    #set it to context object
    product = get_object_or_404(Product, slug=slug)
    context = { 'product': product}

    #render the product info view with this product context object
    return render(request, 'store/product-info.html',context)