from django.shortcuts import render
from .models import Category

# Create your views here.

def store(request):
    #because we have our template folder nested under store we need to add that path here
    return render(request, 'store/store.html')


def categories(request):
    #get all categories from the model
    all_categories = Category.objects.all()
    

    return {'all_categories': all_categories}

