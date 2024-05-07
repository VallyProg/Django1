from django.contrib import admin
from .models import User, Product, Order

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'product', 'quantity')
    list_filter = ('client', 'product')

admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)