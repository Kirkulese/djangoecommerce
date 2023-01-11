from django.urls import path

from . import views

urlpatterns = [
    #main store landing page
    path('',views.store, name='store'),

    #set up individual product path using the slug field 
    path('product/<slug:product_slug>/', views.product_info, name='product-info'),

    #set up search by category
    path('search/<slug:category_slug>', views.list_category, name='list-category'),
]
