from django.contrib import admin

# Register your models here.

from . models import Category, Product

# functions to register admin site
# admin.site.register(Category)

# admin.site.register(Product)

#class to register admin site can use prepopulated fields
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}