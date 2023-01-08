from django.shortcuts import render

# Create your views here.

def store(request):
    #because we have our template folder nested under store we need to add that path here
    return render(request, 'store/store.html')
