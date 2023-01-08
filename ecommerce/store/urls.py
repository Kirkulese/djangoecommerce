from django.urls import path

from . import views

urlpatterns = [
    path('',views.store, name='store'),
    #set up individual product path using the slug field 
    path('product/<slug:slug>/', views.product_info, name='product')
]
